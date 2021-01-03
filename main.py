from zipper import zipper
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from tempfile import NamedTemporaryFile
import scipy.io
import numpy as np
import uvicorn
import pandas as pd
import time
from Mat import Mat
app = FastAPI()


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):

    return {"filename": file.filename}


@app.post("/matToCsv")
async def matToCsv(file: UploadFile = File(...)):
    # content = file.file
    # data = scipy.io.loadmat(content)

    # for i in data:
    #     if '__' not in i and 'readme' not in i:
    #         np.savetxt(("file.csv"), data[i], delimiter=',', fmt=('%s'))
    mat = Mat(file.file)
    files = mat.save()

    zip_filename = zipper(mat.workingDirectory, files)
    return FileResponse(zip_filename)


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost",
                port=8000)
