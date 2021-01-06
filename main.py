from maybe_zipper import maybe_zipper
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import uvicorn
from settings import settings


from classen_ordner.Csv import Csv
from classen_ordner.Mat import Mat

# print(dir(Csv))
app = FastAPI()

folders = []


def updateFolders(obj):
    folders.append(obj)
    if len(folders) > settings["folderlimit"]:
        del folders[0]


@app.post("/convert/{input}/{output}")
async def convert(output: str, input: str, file: UploadFile = File(...)):

    # inputfile mit passender Klasse öffnen
    input_file = eval(input.lower().capitalize())(file.file, file.filename)
    # inputfile umwandeln und speichern
    files = eval(f"input_file.{output}()")
    updateFolders(input_file)
    path, file_name = maybe_zipper(
        input_file.workingDirectory, files, input_file.name)

    return FileResponse(path, filename=file_name)
    # return FileResponse(file, filename=f"test.{output}")


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
