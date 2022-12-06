import os


class PytestDocumentWriter():
    def __init__(self, rootDirectory: str) -> None:
        self.rootDirectory = rootDirectory

    def write_document(self, relative_path: str, content: str):
        print(content)
        file_path = os.path.join(self.rootDirectory, relative_path)
        with open(file_path, 'w') as f:
            f.write(content)
