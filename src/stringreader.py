from io import StringIO


class StringReader:
    _file_str = None

    def __init__(self, content: str) -> None:
        self._file_str = StringIO(content)

    def read_line(self) -> str:
        return self._file_str.readline()
