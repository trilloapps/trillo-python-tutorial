from multimethods import multimethod

from src.collager.model.DataIterator import DataIterator
from src.collager.util.HttpRequestUtil import HttpRequestUtil
from src.io.RunFunction import Proxy

dataBaseEndpoint = "/api/v1.1/data"


def getPage(dataRequestAsMap):
    return Proxy.remoteCall("DSApi", "getPage", dataRequestAsMap)


@multimethod(str, str, str, int, int)
def getDataIterator(className, where, orderBy, start, pageSize):
    return DataIterator(className, where, orderBy, start, pageSize)


@multimethod(int, int, str)
def getDataIterator(start, pageSize, sqlQuery):
    return DataIterator(start, pageSize, sqlQuery)

@multimethod(str, str, int, int, str)
def getDataIterator(appName, dsName, start, pageSize, sqlQuery):
    return DataIterator(appName, dsName, start, pageSize, sqlQuery)


@multimethod(int, int, str, bool)
def getDataIterator(start, pageSize, sqlQuery, orderById):
    return DataIterator(start, pageSize, sqlQuery, orderById)


@multimethod(int, int, str, str, bool)
def getDataIterator(start, pageSize, sqlQuery, idAttrName, orderById):
    return DataIterator(start, pageSize, sqlQuery, idAttrName, orderById)


def get(className, id):
    return HttpRequestUtil.get(dataBaseEndpoint + "/get/" + className + "/" + id)


@multimethod(str, str)
def queryOne(className, query):
    return HttpRequestUtil.get(dataBaseEndpoint + "/queryOne/" + str(className) + "?query=" + str(query))


@multimethod(str, str, bool)
def queryOne(className, query, includeDeleted):
    return HttpRequestUtil.get(
        dataBaseEndpoint + "/queryOne/" + str(className) + "?query=" + str(query) + "&includeDeleted=" + str(
            includeDeleted))


@multimethod(str, str, bool)
def queryMany(className, query, includeDeleted):
    return HttpRequestUtil.get(
        dataBaseEndpoint + "/queryMany/" + str(className) + "?query=" + str(query) + "&includeDeleted=" + str(
            includeDeleted))


@multimethod(str, str)
def queryMany(className, query):
    return HttpRequestUtil.get(
        dataBaseEndpoint + "/queryMany/" + str(className) + "?query=" + str(query))


@multimethod(str)
def queryBySqlStatement(sqlStatement):
    return HttpRequestUtil.get(
        dataBaseEndpoint + "/queryBySqlStatement?sqlStatement=" + sqlStatement)


@multimethod(str, str)
def queryBySqlStatement(dsName, sqlStatement):
    return HttpRequestUtil.get(
        dataBaseEndpoint + "/queryBySqlStatement?sqlStatement=" + sqlStatement + "&dsName=" + dsName)


@multimethod(str, str, dict)
def queryBySqlStatement(dsName, sqlStatement, params):
    return HttpRequestUtil.get(
        dataBaseEndpoint + "/queryBySqlStatement?sqlStatement=" + sqlStatement + "&dsName=" + dsName + "&params=" + str(
            params))


def save(className, entity):
    return HttpRequestUtil.post(
        dataBaseEndpoint + "/save/" + className, entity)


def saveMany(className, entities):
    return HttpRequestUtil.post(
        dataBaseEndpoint + "/saveMany/" + className, entities)


def saveManyIgnoreError(className, entities):
    return HttpRequestUtil.post(
        dataBaseEndpoint + "/saveManyIgnoreError/" + className, entities)


def update(className, id, attrName, value):
    body = {"attrName": attrName,
            "attrValue": value}
    return HttpRequestUtil.post(
        dataBaseEndpoint + "/update/" + className + "/" + id, body)


def updateUsingMap(className, id, updateAttrs):
    return HttpRequestUtil.post(
        dataBaseEndpoint + "/updateUsingMap/" + className + "/" + id, updateAttrs)


def updateMany(className, ids, attrName, value):
    body = {"ids": ids,
            "attrName": attrName,
            "value": value
            }
    return HttpRequestUtil.post(
        dataBaseEndpoint + "/updateMany/" + className, body)


def updateManyUsingMap(className, ids, updateAttrs):
    body = {"ids": ids,
            "updateAttrs": updateAttrs
            }
    return HttpRequestUtil.post(
        dataBaseEndpoint + "/updateManyUsingMap/" + className, body)


def updateByQuery(className, whereClause, nameValueMap):
    body = {"whereClause": whereClause,
            "nameValueMap": nameValueMap
            }
    return HttpRequestUtil.post(
        dataBaseEndpoint + "/updateUsingMapByQuery/" + className, body)


def deleteSingle(className, id, isPermanent):
    return HttpRequestUtil.post(
        dataBaseEndpoint + "/delete/" + className + "/" + str(id) + "?permanent=" + str(isPermanent), {})


def deleteMany(className, ids, isPermanent):
    return HttpRequestUtil.post(
        dataBaseEndpoint + "/deleteMany/" + className + "?permanent=" + str(isPermanent), str(ids))


def deleteByQuery(className, query, isPermanent):
    return HttpRequestUtil.post(
        dataBaseEndpoint + "/deleteByQuery/" + className + "?query=" + str(query) + "&permanent=" + str(isPermanent),
        {})


def bulkOp(className, opName, entities):
    return HttpRequestUtil.post(
        dataBaseEndpoint + "/bulkOp/" + className + "/" + opName, entities)


def executeNamedQuery(queryName, queryParameters, onlyOneRow):
    return HttpRequestUtil.post(
        dataBaseEndpoint + "/executeNamedQuery/" + queryName + "?onlyOneRow=" + str(onlyOneRow), queryParameters)


def executePreparedStatement(dataSourceName, sqlStatement, parameters):
    body = {
        "sqlStatement": sqlStatement,
        "parameters": parameters
    }
    return HttpRequestUtil.post(
        dataBaseEndpoint + "/executePreparedStatement/" + dataSourceName, body)


@multimethod(str, str, dict)
def executeSqlWriteStatement(dataSourceName, sqlStatement, parameters):
    body = {
        "sqlStatement": sqlStatement,
        "parameters": parameters
    }
    return HttpRequestUtil.post(
        dataBaseEndpoint + "/executeSqlWriteStatement/" + dataSourceName, body)


@multimethod(str, str, dict)
def executeSqlWriteStatement(dataSourceName, sqlStatement, parameters):
    body = {
        "sqlStatement": sqlStatement,
        "parameters": parameters
    }
    return HttpRequestUtil.post(
        dataBaseEndpoint + "/executeSqlWriteStatement/" + dataSourceName, body)


@multimethod(str, str)
def executeSqlWriteStatement(dataSourceName, sqlStatement):
    body = {
        "sqlStatement": sqlStatement
    }
    return HttpRequestUtil.post(
        dataBaseEndpoint + "/executeSqlWriteStatement/" + dataSourceName, body)


@multimethod(str, str)
def executeSql(dataSourceName, sqlStatement):
    body = {
        "sqlStatement": sqlStatement
    }
    return HttpRequestUtil.post(
        dataBaseEndpoint + "/executeSql/" + dataSourceName, body)


@multimethod(str, str, dict)
def executeSql(dataSourceName, sqlStatement, parameters):
    body = {
        "sqlStatement": sqlStatement,
        "parameters": parameters
    }
    return HttpRequestUtil.post(
        dataBaseEndpoint + "/executeSql/" + dataSourceName, body)


def tenantByName(tenantName):
    return HttpRequestUtil.get(dataBaseEndpoint + "/tenantByName/" + tenantName)


def tenantByQuery(tenantQuery):
    return HttpRequestUtil.get(dataBaseEndpoint + "/tenantByQuery?tenantQuery=" + tenantQuery)


def getUser(id):
    return HttpRequestUtil.get(dataBaseEndpoint + "/user/" + id)


def userByEmail(email):
    return HttpRequestUtil.get(dataBaseEndpoint + "/userByEmail?email=" + email)


def userByUserId(userId):
    return HttpRequestUtil.get(dataBaseEndpoint + "/userByUserId?userId=" + userId)


def keyValueList(key):
    return HttpRequestUtil.get(dataBaseEndpoint + "/keyValueList?key=" + key)


def valueByKey(key, type):
    return HttpRequestUtil.get(dataBaseEndpoint + "/valueByKey?key=" + key + "&type=" + type)


def emptyTable(className):
    return HttpRequestUtil.get(dataBaseEndpoint + "/emptyTable/" + className)


def saveFileOp(fileId, fileName, folderName, op, functionName, status, message):
    body = {"fileName": fileName,
            "folderName": folderName,
            "op": op,
            "functionName": functionName,
            "status": status,
            "message": message}
    return HttpRequestUtil.post(dataBaseEndpoint + "/saveFileOp/" + fileId, body)


@multimethod(str, str, str, str)
def getFileOp(fileName, folderName, op, functionName):
    return HttpRequestUtil.get(
        dataBaseEndpoint + "/getFileOp?fileName=" + fileName + "&folderName=" + folderName + "&op=" + op + "&functionName=" + functionName)


@multimethod(str, str, str)
def getFileOp(fileName, folderName, op):
    return HttpRequestUtil.get(
        dataBaseEndpoint + "/getFileOp?fileName=" + fileName + "&folderName=" + folderName + "&op=" + op)


@multimethod(str, str, str)
def getFileOpByFileId(fileId, op, functionName):
    return HttpRequestUtil.get(
        dataBaseEndpoint + "/getFileOpByFileId?fileId=" + fileId + "&functionName=" + functionName + "&op=" + op)


@multimethod(str, str)
def getFileOpByFileId(fileId, op):
    return HttpRequestUtil.get(dataBaseEndpoint + "/getFileOpByFileId?fileId=" + fileId + "&op=" + op)


@multimethod(str, str, str, str)
def isFileProcessed(fileName, folderName, op, functionName):
    return HttpRequestUtil.get(
        dataBaseEndpoint + "/isFileProcessed?fileName=" + fileName + "&folderName=" + folderName + "&op=" + op + "&functionName=" + functionName)


@multimethod(str, str, str)
def isFileProcessed(fileName, folderName, op):
    return HttpRequestUtil.get(
        dataBaseEndpoint + "/isFileProcessed?fileName=" + fileName + "&folderName=" + folderName + "&op=" + op)


def incrementCounter(className, counterName):
    return HttpRequestUtil.post(dataBaseEndpoint + "/incrementCounter/" + className + "/" + counterName, {})
