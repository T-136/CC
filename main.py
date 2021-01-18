from classen_ordner.Xlsx import Xlsx
from classen_ordner.Csv import Csv
from classen_ordner.Mat import Mat
from classen_ordner.image import Bild
from classen_ordner.pypandoc import Pypandoc
from maybe_zipper import maybe_zipper
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import uvicorn
from settings import settings
from fastapi.middleware.cors import CORSMiddleware
origins = ["*"]  # TODO: CHANGE ON PRODUCTION

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# print(dir(Csv))


folders = []

'''pandoc[0]=inputformat pandoc[1]=outputformat'''
pandoc_files_dict = ['biblatex, bibtex, commonmark, commonmark_x, creole, csljson, csv, docbook, docx, dokuwiki, epub, fb2, gfm, haddock, html, ipynb, jats, jira, json, latex, man, markdown, markdown_github, markdown_mmd, markdown_phpextra, markdown_strict, mediawiki, muse, native, odt, opml, org, rst, t2t, textile, tikiwiki, twiki, vimwiki', 'asciidoc, asciidoctor, beamer, commonmark, commonmark_x, context, csljson, docbook, docbook4, docbook5, docx, dokuwiki, dzslides, epub, epub2, epub3, fb2, gfm, haddock, html, html4, html5, icml, ipynb, jats, jats_archiving, jats_articleauthoring, jats_publishing, jira, json, latex, man, markdown, markdown_github, markdown_mmd, markdown_phpextra, markdown_strict, mediawiki, ms, muse, native, odt, opendocument, opml, org, pdf, plain, pptx, revealjs, rst, rtf, s5, slideous, slidy, tei, texinfo, textile, xwiki, zimwiki']

def updateFolders(obj):
    folders.append(obj)
    if len(folders) > settings["folderlimit"]:
        del folders[0]


@app.post("/convert/{input}/{output}")
async def convert(output: str, input: str, file: UploadFile = File(...)):

    
    if (input  in pandoc_files_dict[0]) and (output in pandoc_files_dict[1]):
        # datei = eval(input.lower().capitalize())(file.file, file.filename)
        pandoc = Pypandoc(file.file, file.filename)
        files = pandoc.convert(input, output)
        updateFolders(pandoc)        
    else: 

        # inputfile mit passender Klasse
        try:
            input_file = eval(input.lower().capitalize())(filepath=file.file, name=file.filename)
            print(input_file.workingDirectory)
            # inputfile öffnen, umwandeln und speichern
            files = eval(f"input_file.{output.lower()}()")
            updateFolders(input_file)

        except:
            # image conversion
            im = Bild(file.filename, file.file)
            path, bild = im.save(output)
            updateFolders(im)
        return FileResponse(path, filename=bild) 
        


    path, file_name = maybe_zipper(input_file.workingDirectory, files, input_file.name)

    return FileResponse(path, filename=file_name)
    

   
if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost",
                port=8000)
