from multimethods import multimethod
from src.collager.util.Util import Util
from src.collager.util.HttpRequestUtil import HttpRequestUtil

bqBaseEndpoint = "/api/v1.1/bq"


@multimethod(str, str, str)
def createTable(datasetName, tableName, schema):
    body = {
        "datasetName": datasetName,
        "tableName": tableName,
        "schema": schema
    }
    res = HttpRequestUtil.post(bqBaseEndpoint + "/createTable", body)
    return Util.convertToResult(res)


@multimethod(str, str, str, str)
def createTable(datasetName, tableName, bucketName, bucketFileName):
    body = {
        "datasetName": datasetName,
        "tableName": tableName,
        "bucketName": bucketName,
        "bucketFileName": bucketFileName
    }
    res = HttpRequestUtil.post(bqBaseEndpoint + "/createTable", body)
    return Util.convertToResult(res)


@multimethod(str, str, list)
def createTable(datasetName, tableName, classAttrs):
    body = {
        "datasetName": datasetName,
        "tableName": tableName,
        "classAttrs": classAttrs
    }
    res = HttpRequestUtil.post(bqBaseEndpoint + "/createTable", body)
    return Util.convertToResult(res)


@multimethod(str, str, list, list, list)
def createTable(datasetName, tableName, csvSchema, classAttrs, mappings):
    body = {
        "datasetName": datasetName,
        "tableName": tableName,
        "csvSchema": csvSchema,
        "classAttrs": classAttrs,
        "mappings": mappings
    }
    res = HttpRequestUtil.post(bqBaseEndpoint + "/createTable", body)
    return Util.convertToResult(res)


def getBQDataSets():
    return HttpRequestUtil.get(bqBaseEndpoint + "/getBQDataSets")


def getBQTables(datasetName):
    return HttpRequestUtil.get(bqBaseEndpoint + "/getBQTables?datasetName=" + datasetName)


@multimethod(str)
def getTable(datasetAndTableName):
    return HttpRequestUtil.get(bqBaseEndpoint + "/getTable?datasetAndTableName=" + datasetAndTableName)


@multimethod(str, str)
def getTable(datasetName, tableName):
    return HttpRequestUtil.get(bqBaseEndpoint + "/getTable?datasetName=" + datasetName + "&tableName=" + tableName)


@multimethod(str)
def getTableFields(datasetAndTableName):
    res = HttpRequestUtil.get(bqBaseEndpoint + "/getTableFields?datasetAndTableName=" + datasetAndTableName)
    return Util.convertToList(res)


@multimethod(str, str)
def getTableFields(datasetName, tableName):
    res = HttpRequestUtil.get(bqBaseEndpoint + "/getTableFields?datasetName=" + datasetName + "&tableName=" + tableName)
    return Util.convertToList(res)


def executeQuery(queryString):
    body = {
        "queryString": queryString
    }
    res = HttpRequestUtil.post(bqBaseEndpoint + "/executeQuery", body)
    return Util.convertToResult(res)


@multimethod(str, str, str, list, list, list, int)
def importCSVIntoTable(datasetName, tableName, pathToFile, csvSchema, classAttrs, mappings, numberOfRowsToSkip):
    body = {
        "datasetName": datasetName,
        "tableName": tableName,
        "pathToFile": pathToFile,
        "csvSchema": csvSchema,
        "classAttrs": classAttrs,
        "mappings": mappings,
        "numberOfRowsToSkip": numberOfRowsToSkip

    }
    res = HttpRequestUtil.post(bqBaseEndpoint + "/importCSVIntoTable", body)
    return Util.convertToResult(res)


@multimethod(str, str, str, dict, int)
def importCSVIntoTable(datasetName, tableName, pathToFile, schema, numberOfRowsToSkip):
    body = {
        "datasetName": datasetName,
        "tableName": tableName,
        "pathToFile": pathToFile,
        "schema": schema,
        "numberOfRowsToSkip": numberOfRowsToSkip

    }
    res = HttpRequestUtil.post(bqBaseEndpoint + "/importCSVIntoTable", body)
    return Util.convertToResult(res)


@multimethod(str, str, str, str, dict, int)
def importCSVIntoTable(datasetName, tableName, path, fileName, schema, numberOfRowsToSkip):
    body = {
        "datasetName": datasetName,
        "tableName": tableName,
        "path": path,
        "fileName": fileName,
        "schema": schema,
        "numberOfRowsToSkip": numberOfRowsToSkip

    }
    res = HttpRequestUtil.post(bqBaseEndpoint + "/importCSVIntoTable", body)
    return Util.convertToResult(res)


@multimethod(str, str, str)
def exportTableToCSV(datasetName, tableName, pathToFile=None, destinationUri=None):
    if pathToFile is not None:
        body = {
            "datasetName": datasetName,
            "tableName": tableName,
            "pathToFile": pathToFile
        }
    else:
        body = {
            "datasetName": datasetName,
            "tableName": tableName,
            "destinationUri": destinationUri

        }
    res = HttpRequestUtil.post(bqBaseEndpoint + "/exportTableToCSV", body)
    return Util.convertToResult(res)


@multimethod(str, str, str, str)
def exportTableToCSV(datasetName, tableName, path, fileName):
    body = {
        "datasetName": datasetName,
        "tableName": tableName,
        "pathToFile": path,
        "fileName": fileName

    }
    res = HttpRequestUtil.post(bqBaseEndpoint + "/exportTableToCSV", body)
    return Util.convertToResult(res)


def exportTable(datasetName, tableName, destinationUri, dataFormat):
    body = {
        "datasetName": datasetName,
        "tableName": tableName,
        "destinationUr": destinationUri,
        "dataFormat": dataFormat

    }
    res = HttpRequestUtil.post(bqBaseEndpoint + "/exportTable", body)
    return Util.convertToResult(res)


@multimethod(str, list, str, str, str)
def bigQueryToCSV(filePath, columnNames, dataSetName, bqTableName, query):
    body = {
        "filePath": filePath,
        "columnNames": columnNames,
        "dataSetName": dataSetName,
        "bqTableName": bqTableName,
        "query": query

    }
    res = HttpRequestUtil.post(bqBaseEndpoint + "/bigQueryToCSV", body)
    return Util.convertToResult(res)


@multimethod(str, list, str, str, str, str)
def bigQueryToCSV(filePath, columnNames, dataSetName, bqTableName, query, functionName):
    body = {
        "filePath": filePath,
        "columnNames": columnNames,
        "dataSetName": dataSetName,
        "bqTableName": bqTableName,
        "functionName": functionName,
        "query": query

    }
    res = HttpRequestUtil.post(bqBaseEndpoint + "/bigQueryToCSV", body)
    return Util.convertToResult(res)


def getPage(query, start, size):
    return HttpRequestUtil.get(bqBaseEndpoint + "/getPage?query=" + query + "&start=" + str(start) + "&size=" + str(size))


def getBigQueryIterator(query, startIndex, pageSize):
    return HttpRequestUtil.get(
        bqBaseEndpoint + "/getBigQueryIterator?query=" + query + "&startIndex=" + startIndex + "&pageSize=" + pageSize)


def insertRows(datasetName, tableName, list):
    body = {
        "datasetName": datasetName,
        "tableName": tableName,
        "list": list

    }
    res = HttpRequestUtil.post(bqBaseEndpoint + "/insertRows", body)
    return Util.convertToResult(res)


def importCSVbyURIIntoTable(datasetName, tableName, sourceUri, schema, numberOfRowsToSkip):
    body = {
        "datasetName": datasetName,
        "tableName": tableName,
        "sourceUri": sourceUri,
        "schema": schema,
        "numberOfRowsToSkip": numberOfRowsToSkip

    }
    res = HttpRequestUtil.post(bqBaseEndpoint + "/importCSVbyURIIntoTable", body)
    return Util.convertToResult(res)


@multimethod(str, str, str)
def importJSONbyURIIntoTable(datasetName, tableName, sourceUri):
    body = {
        "datasetName": datasetName,
        "tableName": tableName,
        "sourceUri": sourceUri

    }
    res = HttpRequestUtil.post(bqBaseEndpoint + "/importJSONbyURIIntoTable", body)
    return Util.convertToResult(res)


@multimethod(str, str, str, list)
def importJSONbyURIIntoTable(datasetName, tableName, sourceUri, schema):
    body = {
        "datasetName": datasetName,
        "tableName": tableName,
        "sourceUri": sourceUri,
        "schema": list(schema)

    }
    res = HttpRequestUtil.post(bqBaseEndpoint + "/importJSONbyURIIntoTable", body)
    return Util.convertToResult(res)


@multimethod(str, str, str, str)
def createTableFromCSV(datasetName, tableName, bucketName, bucketFileName):
    body = {
        "datasetName": datasetName,
        "tableName": tableName,
        "bucketName": bucketName,
        "bucketFileName": bucketFileName

    }
    res = HttpRequestUtil.post(bqBaseEndpoint + "/createTableFromCSV", body)
    return Util.convertToResult(res)


@multimethod(str, str, str)
def createTableFromCSV(datasetName, tableName, bucketFileName):
    body = {
        "datasetName": datasetName,
        "tableName": tableName,
        "bucketFileName": bucketFileName

    }
    res = HttpRequestUtil.post(bqBaseEndpoint + "/createTableFromCSV", body)
    return Util.convertToResult(res)


def bigQueryToCSVWithScript(filePath, columnNames, dataSetName, bqTableName, query, script, scriptFlavor):
    body = {
        "filePath": filePath,
        "columnNames": columnNames,
        "dataSetName": dataSetName,
        "bqTableName": bqTableName,
        "query": query,
        "script": script,
        "scriptFlavor": scriptFlavor

    }
    res = HttpRequestUtil.post(bqBaseEndpoint + "/bigQueryToCSVWithScript", body)
    return Util.convertToInt(res)
