from settings import settings
from .DataFile import DataFile, Tables
from scipy.io import loadmat
import pandas as pd


class Mat(Tables):
    def to_csv(self):
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
