from dataclasses import dataclass


@dataclass
class SQLite3SchemaColumn:
    cid: int
    name: str
    type: str
    notnull: int
    dflt_value: str
    pk: int