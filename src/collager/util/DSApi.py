from multimethods import multimethod

from src.collager.model.DataIterator import DataIterator
from src.collager.model.DataRequest import DataRequest
from src.collager.model.DataResult import DataResult
from src.collager.util.BaseApi import BaseApi
from src.collager.util.HttpRequestUtil import HttpRequestUtil
from src.io.util.Proxy import Proxy

dataBaseEndpoint = "/api/v1.1/data"


@multimethod(dict)
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

@multimethod(str)
def queryOne(query):
    return BaseApi.remoteCall("DSApi", "queryOne", query)


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
    return BaseApi.remoteCall("DSApi", "queryBySqlStatement", sqlStatement)


@multimethod(str, str)
def queryBySqlStatement(dsName, sqlStatement):
    return HttpRequestUtil.get(
        dataBaseEndpoint + "/queryBySqlStatement?sqlStatement=" + sqlStatement + "&dsName=" + dsName)


@multimethod(str, str, dict)
def queryBySqlStatement(dsName, sqlStatement, params):
    return BaseApi.remoteCall("DSApi", "queryBySqlStatement", dsName, sqlStatement, params)


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
    return BaseApi.remoteCall("DSApi", "update", className, id, dict(updateAttrs))


@multimethod(str, list, str, object)
def updateMany(className, ids, attrName, value):
    return BaseApi.remoteCall("DSApi", "updateMany", className, list(ids), attrName, value)


@multimethod(str, list, dict)
def updateMany(className, ids, updateAttrs):
    return BaseApi.remoteCall("DSApi", "updateMany", className, list(ids), dict(updateAttrs))


def updateByQuery(className, whereClause, nameValueMap):
    return BaseApi.remoteCall("DSApi", "updateByQuery", className, whereClause, dict(nameValueMap))


def deleteSingle(className, id, isPermanent):
    return HttpRequestUtil.post(
        dataBaseEndpoint + "/delete/" + className + "/" + str(id) + "?permanent=" + str(isPermanent), {})


def deleteMany(className, ids, isPermanent):
    return BaseApi.remoteCall("DSApi", "deleteMany", className, list(ids), isPermanent)


def deleteByQuery(className, query, isPermanent):
    return BaseApi.remoteCall("DSApi", "deleteByQuery", className, query, isPermanent)


def bulkOp(className, opName, entities):
    return HttpRequestUtil.post(
        dataBaseEndpoint + "/bulkOp/" + className + "/" + opName, entities)


def executeNamedQuery(queryName, queryParameters, onlyOneRow):
    return BaseApi.remoteCall("DSApi", "executeNamedQuery", queryName, dict(queryParameters), bool(onlyOneRow))


def executePreparedStatement(dsName, sqlStatement, values):
    return BaseApi.remoteCall("DSApi", "executePreparedStatement", dsName, sqlStatement, list(values))


@multimethod(str, str, dict)
def executeSqlWriteStatement(dataSourceName, sqlStatement, parameters):
    return BaseApi.remoteCall("DSApi", "executeSqlWriteStatement", dataSourceName, sqlStatement, parameters)


@multimethod(str, str)
def executeSqlWriteStatement(dataSourceName, sqlStatement):
    return BaseApi.remoteCall("DSApi", "executeSqlWriteStatement", dataSourceName, sqlStatement)


@multimethod(str, str)
def executeSql(dataSourceName, sqlStatement):
    return BaseApi.remoteCall("DSApi", "executeSql", dataSourceName, sqlStatement)


@multimethod(str, str, dict)
def executeSql(dataSourceName, sqlStatement, parameters):
    return BaseApi.remoteCall("DSApi", "executeSql", dataSourceName, sqlStatement, parameters)


def tenantByName(tenantName):
    return BaseApi.remoteCall("DSApi", "tenantByName", tenantName)

def tenantByQuery(tenantQuery):
    return BaseApi.remoteCall("DSApi", "tenantByQuery", tenantQuery)

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
    return BaseApi.remoteCall("DSApi", "emptyTable", className)


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
    return BaseApi.remoteCall("DSApi", "incrementCounter", className, counterName)

def commitTx():
    """
    In dev-env, all DB calls are transactional therefore a transaction can't be committed (not needed).
    This limitation may be removed in the future.
    """
    pass

def rollbackTx():
    """
    In dev-env, all DB calls are transactional therefore a transaction can't be rolled back.
    This limitation may be removed in the future.
    """
    pass


