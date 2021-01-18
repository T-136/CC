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

    def xlsx(self):
        """returns 
            dict with
                filename : csv string
        """
        data = loadmat(self.filepath)
        print(data.keys())
        with pd.ExcelWriter(f"{settings['datafolder']}/{self.workingDirectory}/{self.name}.xlsx") as writer:
            for key in data.keys():
                if key.startswith("__"):
                    pass
                else:
                    print("schlüsel: ", key)
                    print("daten: ", data[key])
                    pd.DataFrame(data[key]).to_excel(writer, sheet_name=key, header=None, index=False)
            FilesDict = {f"{self.name}.xlsx": f"{settings['datafolder']}/{self.workingDirectory}/{self.name}.xlsx"}
        return FilesDict