import uuid
import shutil
from settings import settings
import os
from .file_typ import FilesDict
import pandas as pd


class DataFile:
    def __init__(self, filepath, name):
        self.filepath = filepath
        self.name = name.rsplit(".", maxsplit = 1)[0]
        print(self.name)
        self.workingDirectory = str(uuid.uuid4())

    def save(self):
        print("ES GIBT NOCH KEINE SAVE FUNKTION", self)

    def __del__(self):
        print("i was deleted")
        shutil.rmtree(
            f"{settings['datafolder']}/{self.workingDirectory}", ignore_errors=True)


class Tables(DataFile):
    def xlsx(self):
        '''
        dataFrame to xlsx-format
        '''
        data: pd.DataFrame = self.to_dataFrame()
        print("save")
        os.makedirs(f"{settings['datafolder']}/{self.workingDirectory}")
        data.to_excel(
            f"{settings['datafolder']}/{self.workingDirectory}/{self.name}.xlsx", header=None, index=False)
        # return f"{settings['datafolder']}/{self.workingDirectory}/irgendwas.xlsx"
        return FilesDict({f"{self.name}.xlsx": f"{settings['datafolder']}/{self.workingDirectory}/{self.name}.xlsx"})

    def csv(self):
        '''
        input: dict{filename : csv_string}
        output: dict{filename : csv_datei}
        '''
        dictionary = self.to_csv()
        os.makedirs(f"{settings['datafolder']}/{self.workingDirectory}")
        for filename in dictionary:
            with open(f"{settings['datafolder']}/{self.workingDirectory}/{filename}", "w", newline="") as f:
                f.write(dictionary[filename])
            dictionary[filename] = f"{settings['datafolder']}/{self.workingDirectory}/{filename}"
        return FilesDict(dictionary)
