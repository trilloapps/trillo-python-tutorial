class CoreDSUtil:
    POSTGRESQL = "postgresql"
    MYSQL = "mysql"
    JDBC = "jdbc"
    MICROSOFTSQL = "microsoftsql"

    class AttrType:
        CHAR = "CHAR"
        STRING = "STRING"
        TEXT = "TEXT"
        MEDIUMTEXT = "MEDIUMTEXT"
        LONGTEXT = "LONGTEXT"
        LONGSTRING = "LONGSTRING"
        VARCHAR = "VARCHAR"
        DECIMAL = "DECIMAL"
        NUMERIC = "NUMERIC"
        BOOLEAN = "BOOLEAN"
        BYTE = "BYTE"
        SHORT = "SHORT"
        INTEGER = "INTEGER"
        INT = "INT"
        LONG = "LONG"
        BIGINTEGER = "BIGINTEGER"
        FLOAT = "FLOAT"
        DOUBLE = "DOUBLE"
        BINARY = "BINARY"
        VARBINARY = "VARBINARY"
        LONGVARBINARY = "LONGVARBINARY"
        DATE = "DATE"
        DATETIME = "DATETIME"
        TIME = "TIME"
        TIMESTAMP = "TIMESTAMP"
        BLOB = "BLOB"
        MEDIUMBLOB = "MEDIUMBLOB"
        LONGBLOB = "LONGBLOB"
        JSON = "JSON"
        JSONSTR = "JSONSTR"

    @staticmethod
    def updateLimitClause(query, offset, size, db_type):
        if CoreDSUtil.POSTGRESQL == db_type:
            updated_query_string = f"{query} offset {offset} limit {offset + size}"
        elif CoreDSUtil.MICROSOFTSQL == db_type:
            updated_query_string = f"{query} offset {offset} rows fetch next {size} rows only"
        else:
            updated_query_string = f"{query} limit {offset},{offset + size}"
        return updated_query_string

    @staticmethod
    def as_str(attr_type):
        return attr_type.lower()
