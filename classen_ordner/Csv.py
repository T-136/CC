from scipy.io import loadmat
import io
import pandas as pd
from classen_ordner.DataFile import DataFile, Tables
from settings import settings
import os
import tempfile
import typing


class Csv(Tables):

    def to_dataFrame(self) -> pd.DataFrame:
        data = io.BytesIO(self.filepath.read())
        data = pd.read_csv(data, delimiter=";", header=None)
        return data

    # def xlsx(self):
    #     fil = self.toXlsx()
    #     print("save")
    #     os.makedirs(f"{settings['datafolder']}/{self.workingDirectory}")
    #     fil.to_excel(
    #         f"{settings['datafolder']}/{self.workingDirectory}/irgendwas.xlsx", header=None, index=False)
    #     return f"{settings['datafolder']}/{self.workingDirectory}/irgendwas.xlsx"
