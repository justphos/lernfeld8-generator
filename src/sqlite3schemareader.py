from sqlite3 import Connection

from sqlite3schemacolumn import SQLite3SchemaColumn
from sqlite3schematable import SQLite3SchemaTable


class SQLite3SchemaReader:
    def __init__(self, database_connection: Connection):
        self.cursor = database_connection.cursor()

    def get_tables(self):
        table_names = self._select_all_table_names()
        for table in table_names:
            table_infos = self._get_table_info(table[0])
            schema_table = SQLite3SchemaTable(
                name=table[0],
                columns=[
                    SQLite3SchemaColumn(
                        cid=table_info[0],
                        name=table_info[1],
                        type=table_info[2],
                        notnull=table_info[3],
                        dflt_value=table_info[4],
                        pk=table_info[5]
                    ) for table_info in table_infos
                ]
            )
            yield schema_table

    def _select_all_table_names(self) -> list:
        res = self.cursor.execute("""
        SELECT name FROM 
        (SELECT * FROM sqlite_schema)
        WHERE type='table'
        ORDER BY name""")
        return res.fetchall()

    def _get_table_info(self, table_name: str) -> list:
        res = self.cursor.execute(f"PRAGMA table_info({table_name})")
        return res.fetchall()
