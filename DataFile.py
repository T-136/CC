import uuid
import shutil
from settings import settings


class DataFile:
    def __init__(self, filepath):
        self.filepath = filepath
        self.workingDirectory = str(uuid.uuid4())

    def save(self):
        print("ES GIBT NOCH KEINE SAVE FUNKTION", self)

    def __del__(self):
        print("i was deleted")
        shutil.rmtree(
            f"{settings['datafolder']}/{self.workingDirectory}", ignore_errors=True)

    # @property                                                                                                                          
    # def readable(self):                                                                                                                
    #     return self._file.readable   
