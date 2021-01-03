import zipfile
from settings import settings


def zipper(folder, files):
    with zipfile.ZipFile(f"{settings['datafolder']}/{folder}/temp.zip", "w") as z:
        for filename in files:
            z.write(filename)
    return f"{settings['datafolder']}/{folder}/temp.zip"
