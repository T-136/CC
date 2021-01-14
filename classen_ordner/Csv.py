from scipy.io import loadmat
import io
import pandas as pd
from classen_ordner.DataFile import DataFile, Tables
from settings import settings
from scipy.io import savemat


class Csv(Tables):

    def to_dataFrame(self) -> pd.DataFrame:
        data = io.BytesIO(self.filepath.read())
        data = pd.read_csv(data, delimiter=";", header=None)
        return data

    # def mat(self):
    #     '''pd.DataFrame  to mat
    #     '''
    #     dataFrame = self.to_dataFrame()
    #     mdict = dataFrame.to_dict()
    #     savemat(f"{settings['datafolder']}/{self.workingDirectory}/{self.name}.mat", mdict)
    #     files = [f"{settings['datafolder']}/{self.workingDirectory}/{self.name}.xlsx"]
    #     return files


