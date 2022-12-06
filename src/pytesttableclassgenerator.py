from indent import Indent
from pytestbuilder import PytestBuilder
from sqlite3schematable import SQLite3SchemaTable


class PytestTableClassGenerator:
    def __init__(self, table: SQLite3SchemaTable):
        self.table = table

    def generate(self) -> str:
        indent = Indent()
        builder = PytestBuilder()

        builder.append_line(indent, "from dataclasses import dataclass")
        builder.append_line(indent)
        builder.append_line(indent)
        builder.append_line(indent, "@dataclass")
        builder.append_line(
            indent, f"class {self.table.name.lower().capitalize()}:")

        indent.increment()

        for column in self.table.columns:
            builder.append_line(
                indent, f"{column.name.lower()}: {column.type.lower()}")

        indent.decrement()

        return str(builder)
