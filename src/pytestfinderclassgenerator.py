from indent import Indent
from pytestbuilder import PytestBuilder
from sqlite3schematable import SQLite3SchemaTable


class PytestFinderClassGenerator:
    def __init__(self, table: SQLite3SchemaTable):
        self.table = table

    def generate(self) -> str:
        indent = Indent()
        builder = PytestBuilder()

        builder.append_line(indent, "from typing import Callable, List")
        builder.append_line(indent)
        builder.append_line(indent, f"from generated.entities.{self.table.name.lower()}_generated import {self.table.name.lower().capitalize()}")
        builder.append_line(indent)
        builder.append_line(indent)
        builder.append_line(
            indent, f"class {self.table.name.lower().capitalize()}Finder:")

        indent.increment()

        builder.append_line(
            indent, f"def __init__(self, {self.table.name.lower()}_factory: Callable[..., {self.table.name.lower().capitalize()}]) -> None:")

        indent.increment()

        builder.append_line(
            indent, f"self._{self.table.name.lower()}_factory = {self.table.name.lower()}_factory")

        indent.decrement()

        builder.append_line(indent)
        builder.append_line(
            indent, f"def find_all(self) -> List[{self.table.name.lower().capitalize()}]:")

        indent.increment()

        builder.append_line(indent, "raise NotImplementedError()")

        indent.decrement()
        indent.decrement()

        return str(builder)
