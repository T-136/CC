from PIL import Image
from settings import settings
import uuid
import os
from classen_ordner.DataFile import DataFile
import shutil

class Bild(DataFile):
    def __init__(self, name, content):
        self.content = Image.open(content)
        self.name = name
        self.workingDirectory = str(uuid.uuid4())
        print(self.workingDirectory)
        os.makedirs(f"{settings['datafolder']}/{self.workingDirectory}")
    
    def save(self, out_format):
        os.makedirs(f"{settings['datafolder']}/{self.workingDirectory}")
        self.content.save(f"{settings['datafolder']}/{self.workingDirectory}/{self.name}.{out_format}")
        return f"{settings['datafolder']}/{self.workingDirectory}/{self.name}.{out_format}", f"{self.name}.{out_format}"
    
    def __del__(self):
        print("i was deleted bild")
        shutil.rmtree(
            f"{settings['datafolder']}/{self.workingDirectory}", ignore_errors=True)


