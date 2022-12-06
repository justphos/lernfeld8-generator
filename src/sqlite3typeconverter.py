class SQLite3TypeConverter:        
    def convert(sqlite3_type) -> str:
        match sqlite3_type:
            case "NULL":
                return "None"
            case "INTEGER":
                return "int"
            case "REAL":
                return "float"
            case "TEXT":
                return "str"
            case "BLOB":
                return "bytes"
            case _:
                raise NotImplementedError(sqlite3_type)