import uuid


class DataFile:
    def __init__(self, filepath):
        self.filepath = filepath
        self.workingDirectory = str(uuid.uuid4())
