from zipper import zipper
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import scipy.io
import numpy as np
import uvicorn
import pandas as pd
from settings import settings
from Mat import Mat
from Mat import Csv

app = FastAPI()

folders = []


def updateFolders(obj):
    folders.append(obj)
    if len(folders) > settings["folderlimit"]:
        del folders[0]


@app.get("/convert/{input}/{output}")
async def convert(file: UploadFile = File(...), input, output):
    
    return {"item_id": item_id}


@app.post("/csvToXlsx")
async def csvToXlsx(file: UploadFile = File(...)):
    csv = Csv(file.file)
    # print(csv.file.read)
    files = csv.save()
    updateFolders(csv)
    # zip_filename = zipper(csv.workingDirectory, files)
    return FileResponse(files, filename="test.xlsx")


@app.post("/matToCsv")
async def matToCsv(file: UploadFile = File(...)):
    mat = Mat(file.file)
    files = mat.save()
    updateFolders(mat)
    zip_filename = zipper(mat.workingDirectory, files)
    return FileResponse(zip_filename, filename="test.zip")

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost",
                port=8000)
