from scipy.io import loadmat
import io
import pandas as pd
from classen_ordner.DataFile import DataFile, Tables
from settings import settings


class Csv(Tables):

    def to_dataFrame(self) -> pd.DataFrame:
        data = io.BytesIO(self.filepath.read())
        data = pd.read_csv(data, delimiter=";", header=None)
        return data

