from PIL import Image
from settings import settings
import uuid
import os
from classen_ordner.DataFile import DataFile

class Bild(DataFile):
    def __init__(self, name, content):
        self.content = Image.open(content)
        self.name = name
        self.workingDirectory = str(uuid.uuid4())
    
    def save(self, out_format):
        os.makedirs(f"{settings['datafolder']}/{self.workingDirectory}")
        self.content.save(f"{settings['datafolder']}/{self.workingDirectory}/{self.name}.{out_format}")
        return f"{settings['datafolder']}/{self.workingDirectory}/{self.name}.{out_format}", f"{self.name}.{out_format}"


# class Jpg(Image):
#     def png(self):
#         self.content.save(f"{settings['datafolder']}/{self.workingDirectory}/{self.name}.png")