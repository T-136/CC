from zipper import zipper
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import scipy.io
import numpy as np
import uvicorn
import pandas as pd
from settings import settings
from Mat import Mat
app = FastAPI()

folders = []


def updateFolders(obj):
    folders.append(obj)
    if len(folders) > settings["folderlimit"]:
        del folders[0]


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):

    return {"filename": file.filename}


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
