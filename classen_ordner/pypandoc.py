import pypandoc
from settings import settings
from .DataFile import DataFile, Tables
from .file_typ import FilesDict
import shutil


class Pypandoc(DataFile):

    def convert(self, input, output):
        with open(f"{settings['datafolder']}/{self.workingDirectory}/{self.name}.{input}", "wb") as file:
            shutil.copyfileobj(self.filepath, file)
        pypandoc.convert_file(
            f"{settings['datafolder']}/{self.workingDirectory}/{self.name}.{input}", output, outputfile=f"{settings['datafolder']}/{self.workingDirectory}/{self.name}.{output}")
        return FilesDict({f"{self.name}.{output}": f"{settings['datafolder']}/{self.workingDirectory}/{self.name}.{output}"})

    # output = pypandoc.convert_file('somefile.md', 'docx', outputfile="somefile.docx")
