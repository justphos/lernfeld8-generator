from io import StringIO


class StringBuilder:
    _file_str = None

    def __init__(self, content: str = "") -> None:
        self._file_str = StringIO()
        self._file_str.write(content)

    def append(self, content: str):
        self._file_str.write(content)

    def append_line(self, content: str):
        self._file_str.write(content + "\n")

    def clear(self):
        self._file_str = StringIO()

    def __str__(self) -> str:
        return self._file_str.getvalue()
