import pandas as pd
from classen_ordner.DataFile import DataFile, Tables
from settings import settings
import io


class Xlsx(Tables):

    def to_dataFrame(self) -> pd.DataFrame:
        '''
        returns {sheet_name: dataframe}
        '''
        df = io.BytesIO(self.filepath.read())
        df = pd.read_excel(df, sheet_name=None)
        dictionary = df
        for sheet in list(df):
            if dictionary[sheet].empty:
                del dictionary[sheet]     
        return dictionary

    def to_csv(self) -> dict:
        """returns 
            dict with
            filename : csv string
        """
        data : pd.DataFrame = self.to_dataFrame()
        print(data)
        files = {}
        for key in data.keys():
            print(key)
            csv_string = data[key].to_csv(index=False, header=False, sep=';')
            print(csv_string)
            files[f"{key}.csv"] = csv_string
        return files
