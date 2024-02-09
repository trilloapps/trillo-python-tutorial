from typing import List, Dict, Any, Union

from src.collager.pojo.ResultApi import Result
from src.collager.util import CSVApi
from src.collager.util.CSVConst import CSVConst


class CSVIterator:
    def __init__(self, fileName: str, query: str, startIndex: int, pageSize: int):
        self.iteratorEnded = False
        self.startIndex = startIndex
        self.pageSize = pageSize
        self.query = query
        self.fileName = fileName
        self.separatorChar = CSVConst.DEFAULT_SEPARATOR_CHAR
        self.columnNames = []
        self.columnNameLine = CSVConst.DEFAULT_COLUMN_NAME_LINE

    def __init__(self, fileName: str, columnNames: List[str], query: str, startIndex: int, pageSize: int):
        self.iteratorEnded = False
        self.startIndex = startIndex
        self.pageSize = pageSize
        self.query = query
        self.fileName = fileName
        self.separatorChar = CSVConst.DEFAULT_SEPARATOR_CHAR
        self.columnNames = columnNames
        self.columnNameLine = CSVConst.DEFAULT_COLUMN_NAME_LINE

    def __init__(self, fileName: str, columnNames: List[str], columnNameLine: int, query: str, startIndex: int, pageSize: int):
        self.iteratorEnded = False
        self.startIndex = startIndex
        self.pageSize = pageSize
        self.query = query
        self.fileName = fileName
        self.separatorChar = CSVConst.DEFAULT_SEPARATOR_CHAR
        self.columnNames = columnNames
        self.columnNameLine = columnNameLine

    def __init__(self, fileName: str, separatorChar: str, query: str, startIndex: int, pageSize: int):
        self.iteratorEnded = False
        self.startIndex = startIndex
        self.pageSize = pageSize
        self.query = query
        self.fileName = fileName
        self.separatorChar = separatorChar
        self.columnNames = []
        self.columnNameLine = CSVConst.DEFAULT_COLUMN_NAME_LINE

    def __init__(self, fileName: str, separatorChar: str, columnNames: List[str], query: str, startIndex: int, pageSize: int):
        self.iteratorEnded = False
        self.startIndex = startIndex
        self.pageSize = pageSize
        self.query = query
        self.fileName = fileName
        self.separatorChar = separatorChar
        self.columnNames = columnNames
        self.columnNameLine = CSVConst.DEFAULT_COLUMN_NAME_LINE

    def __init__(self, fileName: str, separatorChar: str, columnNames: List[str], columnNameLine: int, query: str, startIndex: int, pageSize: int):
        self.iteratorEnded = False
        self.startIndex = startIndex
        self.pageSize = pageSize
        self.query = query
        self.fileName = fileName
        self.separatorChar = separatorChar
        self.columnNames = columnNames
        self.columnNameLine = columnNameLine

    def getPage(self) -> Union[Dict[str, Any], Result]:
        if self.iteratorEnded:
            return Result.getFailedResult("Iterator reached the end of the result list")
        l = CSVApi.csvGetPage(self.fileName, self.separatorChar, self.columnNames, self.columnNameLine, self.query, self.startIndex, self.pageSize)
        self.startIndex += len(l)
        if len(l) < self.pageSize:
            self.iteratorEnded = True
        return l

    def hasNextPage(self) -> bool:
        return not self.iteratorEnded

    def close(self):
        self.iteratorEnded = True
        # no need to close, this is a part of the remote client.
        # The actual processing is done on the server.
        # The remote server always closes the iterator before returning.
        # It creates a new iterator for each call. It is inefficient but OK for the development purpose.
