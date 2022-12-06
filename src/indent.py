from stringbuilder import StringBuilder
from stringreader import StringReader


class Indent:
    def __init__(self) -> None:
        self.level = 0

    def increment(self):
        self.level += 1

    def decrement(self):
        self.level -= 1
        if self.level == 0:
            self.level = 0

    def reset(self):
        self.level = 0

    def wrap(self, subject: str) -> str:
        builder = StringBuilder()
        reader = StringReader(subject)
        line = reader.read_line()
        while len(line) > 0:
            if not line.startswith('//'):
                builder.append(' ' * self.level * 4)
            builder.append_line(line.rstrip('\n'))
            line = reader.read_line()

        return str(builder)

    def __str__(self) -> str:
        return ' ' * self.level * 4
