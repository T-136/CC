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


def updateFolders(obj):
    folders.append(obj)
    if len(folders) > settings["folderlimit"]:
        del folders[0]


@app.post("/convert/{input}/{output}")
async def convert(output: str, input: str, file: UploadFile = File(...)):

    # inputfile mit passender Klasse
    try:
        input_file = eval(input.lower().capitalize())(file.file, file.filename)
        # inputfile öffnen, umwandeln und speichern
        files = eval(f"input_file.{output.lower()}()")
        updateFolders(input_file)

    # except:
    #     # datei = eval(input.lower().capitalize())(file.file, file.filename)
    #     pandoc = Pypandoc(file.file, file.filename)
    #     files = pandoc.convert(input, output)
    #     updateFolders(pandoc)
    
    except:
        # image conversion
        im = Bild(file.filename, file.file)
        path, bild = im.save(output)


    # path, file_name = maybe_zipper(
    #     input_file.workingDirectory, files, input_file.name)

    return FileResponse(path, filename=bild)

    # return FileResponse(path, filename=file_name)


# @app.post("/csvToXlsx")
# async def csvToXlsx(file: UploadFile = File(...)):
#     csv = Csv(file.file)
#     # print(csv.file.read)
#     files = csv.save()
#     updateFolders(csv)
#     # zip_filename = zipper(csv.workingDirectory, files)
#     return FileResponse(files, filename="test.xlsx")


# @app.post("/matToCsv")
# async def matToCsv(file: UploadFile = File(...)):
#     mat = Mat(file.file)
#     files = mat.save()
#     updateFolders(mat)
#     zip_filename = zipper(mat.workingDirectory, files)
#     return FileResponse(zip_filename, filename="test.zip")

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost",
                port=8000)
