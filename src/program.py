from pytestdocumentwriter import PytestDocumentWriter
from pytestgenerator import PytestGenerator


if __name__ == '__main__':
    pytestgenerator = PytestGenerator()
    pytestgenerator.generate_files(PytestDocumentWriter(
        rootDirectory="/home/b00d8/pytest-generator/pytest-generator/generated/"))
