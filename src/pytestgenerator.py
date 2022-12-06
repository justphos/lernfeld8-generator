from sqlite3 import Error, connect
from typing import Type

from pytestdocument import PytestDocument
from pytestdocumentwriter import PytestDocumentWriter
from pytesttableclassgenerator import PytestTableClassGenerator
from sqlite3schemareader import SQLite3SchemaReader
from pytestfinderclassgenerator import PytestFinderClassGenerator


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


class PytestGenerator:

    def __init__(self) -> None:
        pass

    def generate_files(self, client_document_writer: Type[PytestDocumentWriter]):
        schema_reader = SQLite3SchemaReader(create_connection(r'test.db'))
        for table in schema_reader.get_tables():
            table_gen = PytestTableClassGenerator(table)
            self.write_to_document(
                client_document_writer,
                "entities/" + table.name.lower() + "_generated.py",
                table_gen.generate()
            )
            
            finder_gen = PytestFinderClassGenerator(table)
            self.write_to_document(
                client_document_writer,
                "finders/" + table.name.lower() + "finder_generated.py",
                finder_gen.generate()
            )

    def write_to_document(self, document_writer: Type[PytestDocumentWriter], relative_path: str, contents: str):
        document = PytestDocument()
        document.append_line(contents)
        document_writer.write_document(relative_path, str(document))
        print("writing")
