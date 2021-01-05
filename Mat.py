from scipy.io import loadmat
import io
import pandas as pd
from DataFile import DataFile
from settings import settings
import os
import tempfile
import csv


class Mat(DataFile):
    def toCSV(self):
        """returns 
            dict with
                filename : csv string
        """
        print(self.filepath)
        data = loadmat(self.filepath)
        files = {}
        for key in data.keys():
            if key.startswith("__"):
                pass
            else:
                csv_string = pd.DataFrame(data[key]).to_csv(
                    index=False, header=False)
                files[f"{key}.csv"] = csv_string
        return files

    def save(self):
        files = self.toCSV()
        os.makedirs(f"{settings['datafolder']}/{self.workingDirectory}")
        for filename in files:
            with open(f"{settings['datafolder']}/{self.workingDirectory}/{filename}", "w", newline="") as f:
                f.write(files[filename])
        return files


class Csv(DataFile):
    def toXlsx(self):
        print("test")
        data = io.BytesIO(self.filepath.read())
        # data = csv.reader(self.filepath, delimiter=";")
        data = pd.read_csv(data, delimiter=";")
        # data.to_excel("t.xlsx", header=None, index=False)
        return data

    def save(self):
        fil = self.toXlsx()
        print("save")
        os.makedirs(f"{settings['datafolder']}/{self.workingDirectory}")
        fil.to_excel(
            f"{settings['datafolder']}/{self.workingDirectory}/irgendwas.xlsx", header=None, index=False)
        return f"{settings['datafolder']}/{self.workingDirectory}/irgendwas.xlsx"

# data = pd.read_csv("test.csv", delimiter =";")
# print(data)
# data.to_excel("t.xlsx", header=None, index=False)
