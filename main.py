from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from tempfile import NamedTemporaryFile
import scipy.io
import numpy as np
import uvicorn
import pandas as pd
import time
app = FastAPI()


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):

    return {"filename": file.filename}


@app.post("/matToCsv")
async def matToCsv(file: UploadFile = File(...)):
    content = file.file
    data = scipy.io.loadmat(content)

    for i in data:
        if '__' not in i and 'readme' not in i:
            np.savetxt(("file.csv"), data[i], delimiter=',', fmt=('%s'))
    return FileResponse("file.csv")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0",
                port=8000)
