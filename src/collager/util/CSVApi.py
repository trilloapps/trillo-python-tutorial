from multimethods import multimethod
from src.collager.util.Util import Util
from src.collager.util.BaseApi import BaseApi
from src.collager.util.HttpRequestUtil import HttpRequestUtil

csvBaseEndpoint = "/api/v1.1/csv"


@multimethod(str)
def csvGetAllRows(filePath):
    res = HttpRequestUtil.get(csvBaseEndpoint + "/csvGetAllRows?filePath=" + str(filePath))
    return Util.convertToListOfDict(res)


@multimethod(str, str)
def csvGetAllRows(filePath, separator):
    res = HttpRequestUtil.get(csvBaseEndpoint + "/csvGetAllRows?filePath=" + str(filePath) + "&separator=" + str(separator))
    return Util.convertToListOfDict(res)


@multimethod(str, str, list)
def csvGetAllRows(filePath, separator, columnNames):
    res = HttpRequestUtil.get(
        csvBaseEndpoint + "/csvGetAllRows?filePath=" + str(filePath) + "&separator=" + str(separator) + "&columnNames=" + str(columnNames))
    return Util.convertToListOfDict(res)


@multimethod(str, str, list, int)
def csvGetAllRows(filePath, separator, columnNames, columnNameLine):
    res = HttpRequestUtil.get(
        csvBaseEndpoint + "/csvGetAllRows?filePath=" + str(filePath) + "&separator=" + str(separator) + "&columnNames=" + str(columnNames) + "&columnNameLine=" + str(columnNameLine))
    return Util.convertToListOfDict(res)


@multimethod(str, str, list, int, str, int, int)
def csvGetPage(fileName, separator, columnNames, columnNameLine, query, startIndex, pageSize):
    if len(separator) == 1:
        res = HttpRequestUtil.get(
            csvBaseEndpoint + "/csvGetPage?fileName=" + str(fileName) + "&separatorChar=" + str(separator) + "&columnNames=" + str(columnNames) + "&columnNameLine=" + str(columnNameLine) + "&query=" + str(query) + "&startIndex=" + str(startIndex) + "&pageSize=" + str(pageSize))
    else:
        res = HttpRequestUtil.get(
            csvBaseEndpoint + "/csvGetPage?fileName=" + str(fileName) + "&separatorStr=" + str(separator) + "&columnNames=" + str(columnNames) + "&columnNameLine=" + str(columnNameLine) + "&query=" + str(query) + "&startIndex=" + str(startIndex) + "&pageSize=" + str(pageSize))
    return Util.convertToListOfDict(res)


@multimethod(str, str, list, int, list)
def csvWriteFile(fileName, separator, columnNames, columnNameLine, rows):
    if len(separator) == 1:
        body = {
            "fileName": fileName,
            "separatorChar": separator,
            "columnNames": columnNames,
            "columnNameLine": columnNameLine,
            "rows": rows
        }
        res = HttpRequestUtil.post(csvBaseEndpoint + "/csvWriteFile", body)
    else:
        body = {
            "fileName": fileName,
            "separatorStr": separator,
            "columnNames": columnNames,
            "columnNameLine": columnNameLine,
            "rows": rows
        }
    return Util.convertToResult(res)


@multimethod(str, list)
def getCSVWriter(fileName, columnNames):
    return HttpRequestUtil.get(csvBaseEndpoint + "/csvWriteFile?fileName=" + str(fileName) + "&columnNames=" + str(columnNames))


@multimethod(str, str, list)
def getCSVWriter(fileName, separatorChar, columnNames):
    return HttpRequestUtil.get(
        csvBaseEndpoint + "/csvWriteFile?fileName=" + str(fileName) + "&separatorChar=" + str(separatorChar) + "&columnNames=" + str(columnNames))


@multimethod(str, str, list, int)
def getCSVWriter(fileName, separatorChar, columnNames, columnNameLine):
    return HttpRequestUtil.get(
        csvBaseEndpoint + "/csvWriteFile?fileName=" + str(fileName) + "&separatorChar=" + str(separatorChar) + "&columnNames=" + str(columnNames) + "&columnNameLine=" + str(columnNameLine))
