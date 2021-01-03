from scipy.io import loadmat
import pandas as pd
from DataFile import DataFile
from settings import settings
import os


class Mat(DataFile):
    def toCSV(self):
        """returns 
            dict with
                filename : csv string
        """
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
