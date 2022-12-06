from typing import Type

from indent import Indent
from stringbuilder import StringBuilder


class PytestBuilder:
    _string_builder = None

    def __init__(self) -> None:
        self._string_builder = StringBuilder()

    def append_line(self, indent: Type[Indent], line: str = ""):
        self._string_builder.append_line(str(indent) + line)

    def append(self, content: str):
        self._string_builder.append(content)

    def clear(self):
        self._string_builder.clear()

    def __str__(self) -> str:
        return str(self._string_builder)
