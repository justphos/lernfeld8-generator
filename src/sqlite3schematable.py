from dataclasses import dataclass
from typing import List

from sqlite3schemacolumn import SQLite3SchemaColumn


@dataclass
class SQLite3SchemaTable:
    name: str
    columns: List[SQLite3SchemaColumn]
