from scipy.io import loadmat
import numpy
import pandas as pd

data = loadmat('testdatei.mat')
print(data["AreaHighFieldNMR"])

# print(data.keys())
for key in data.keys():
    if key.startswith("__"):
        print(key)
    else:
        print("Super duper key", key)
        pd.DataFrame(data[key]).to_csv(
            f"{key}.csv", index=False, header=False)


class DataFile:
    def __init__(self, file):
        self.file = file


class Mat(DataFile):

    def toCSV(self):
        """Gives back csv file for every table"""
        data = loadmat(self.file)
        for key in data.keys():
            if key.startswith("__"):
                print(key)
            else:
                print("Super duper key", key)
                pd.DataFrame(data[key]).to_csv(
                    f"{key}.csv", index=False, header=False)
        return []
