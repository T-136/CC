import zipfile
from settings import settings
from classen_ordner.file_typ import FilesDict


def maybe_zipper(folder, files: FilesDict, name: str) -> (str, str):
    '''
    sören ist dumm
    list mehere files zippen, 
    eine file einzeln returned
    '''
    if len(files) > 1:
        with zipfile.ZipFile(f"{settings['datafolder']}/{folder}/{name}.zip", "w") as z:
            for filename in files:
                z.write(
                    f"{settings['datafolder']}/{folder}/{filename}", arcname=filename)
        return f"{settings['datafolder']}/{folder}/{name}.zip", f"{name}.zip"
    else:

        return (files[list(files.keys())[0]], list(files.keys())[0])
