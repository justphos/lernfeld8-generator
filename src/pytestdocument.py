from indent import Indent
from pytestbuilder import PytestBuilder
from stringbuilder import StringBuilder


class PytestDocument:
    _string_builder = None

    def __init__(self):
        self._string_builder = StringBuilder()

    def append_line(self, content: str):
        print(content)
        return self._string_builder.append_line(content)

    def __str__(self) -> str:
        indent = Indent()
        print("----------------")
        builder = PytestBuilder()
        builder.append_line(indent, "# ----------------")
        builder.append_line(indent, "# Automatically generated document")
        builder.append_line(indent, "# ----------------")
        builder.append(indent.wrap(str(self._string_builder)))

        return str(builder)
