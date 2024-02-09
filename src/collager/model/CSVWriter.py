from typing import List, Dict

from src.collager.util import CSVApi
from src.collager.util.CSVConst import CSVConst
from src.collager.util.LogApi import Log


class CSVWriter:
    def __init__(self, fileName: str, columnNames: List[str], separatorChar: str = CSVConst.DEFAULT_SEPARATOR_CHAR, columnNameLine: int = CSVConst.DEFAULT_COLUMN_NAME_LINE):
        self.fileName = fileName
        self.separatorChar = separatorChar
        self.columnNames = columnNames
        self.columnNameLine = columnNameLine
        self.rows: List[Dict[str, object]] = []

    def addRow(self, m: Dict[str, object]):
        self.rows.append(m)

    def addRows(self, l: List[Dict[str, object]]):
        self.rows.extend(l)

    def close(self):
        result = CSVApi.csvWriteFile(self.fileName, self.separatorChar, self.columnNames, self.columnNameLine, self.rows)
        if result.isFailed():
            Log.error("Failed to write the csv file, error: " + result.getMessage())
        else:
            Log.info("Successfully written CSV file")
