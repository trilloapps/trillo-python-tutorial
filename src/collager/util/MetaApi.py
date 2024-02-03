from multimethods import multimethod
from src.collager.util import Util
from src.collager.util.HttpRequestUtil import HttpRequestUtil

metaBaseEndpoint = "/api/v1.1/meta"


def getAppDataDir():
    res = HttpRequestUtil.get(metaBaseEndpoint + "/getAppDataDir")
    return HttpRequestUtil.HttpResponseToString(res)


@multimethod(str)
def getClasses(filter):
    res = HttpRequestUtil.get(metaBaseEndpoint + "/getClasses?filter=" + filter)
    return Util.convertToList(res)


@multimethod(str, str)
def getClasses(dsName, filter):
    res = HttpRequestUtil.get(metaBaseEndpoint + "/getClasses?dsName=" + dsName + "&filter=" + filter)
    return Util.convertToList(res)


@multimethod(str, str, str)
def getClasses(dsName, schemaName, filter):
    res = HttpRequestUtil.get(
        metaBaseEndpoint + "/getClasses?dsName=" + dsName + "&schemaName=" + schemaName + "&filter=" + filter)
    return Util.convertToList(res)


@multimethod(str)
def getClassNames(filter):
    res = HttpRequestUtil.get(metaBaseEndpoint + "/getClassNames?filter=" + filter)
    return Util.convertToList(res)


@multimethod(str, str)
def getClassNames(dsName, filter):
    res = HttpRequestUtil.get(metaBaseEndpoint + "/getClassNames?dsName=" + dsName + "&filter=" + filter)
    return Util.convertToList(res)


@multimethod(str, str, str)
def getClassNames(dsName, schemaName, filter):
    res = HttpRequestUtil.get(
        metaBaseEndpoint + "/getClassNames?dsName=" + dsName + "&schemaName=" + schemaName + "&filter=" + filter)
    return Util.convertToList(res)


def getClass(className):
    res = HttpRequestUtil.get(metaBaseEndpoint + "/getClass?className=" + className)
    return HttpRequestUtil.HttpResponseToString(res)


@multimethod(str)
def getDataSources(filter):
    res = HttpRequestUtil.get(
        metaBaseEndpoint + "/getDataSources?filter=" + filter)
    return Util.convertToList(res)


@multimethod(str, str)
def getDataSources(appName, filter):
    res = HttpRequestUtil.get(
        metaBaseEndpoint + "/getDataSources?appName=" + appName + "&filter=" + filter)
    return Util.convertToList(res)


@multimethod(str)
def getDataSourceNames(filter):
    res = HttpRequestUtil.get(
        metaBaseEndpoint + "/getDataSourceNames?filter=" + filter)
    return Util.convertToList(res)


@multimethod(str, str)
def getDataSourceNames(appName, filter):
    res = HttpRequestUtil.get(
        metaBaseEndpoint + "/getDataSourceNames?appName=" + appName + "&filter=" + filter)
    return Util.convertToList(res)


def getDataSource(dsName):
    res = HttpRequestUtil.get(metaBaseEndpoint + "/getDataSource?dsName=" + dsName)
    return HttpRequestUtil.HttpResponseToString(res)


def getClassM(className):
    res = HttpRequestUtil.get(metaBaseEndpoint + "/getClassM?className=" + className)
    return HttpRequestUtil.HttpResponseToString(res)


def saveClass(className, clsM):
    body = {
        "className": className,
        "clsM": clsM
    }
    return HttpRequestUtil.post(metaBaseEndpoint + "/saveClass", body)


def updateClassVisibility(className, visibility):
    body = {
        "className": className,
        "visibility": visibility
    }
    return HttpRequestUtil.post(metaBaseEndpoint + "/updateClassVisibility", body)


def getSchemaForDataStudio(className, includeAllSysAttrs):
    res = HttpRequestUtil.get(
        metaBaseEndpoint + "/getSchemaForDataStudio?className=" + className + "&includeAllSysAttrs=" + includeAllSysAttrs)
    return Util.convertToListOfDict(res)


def getDomainFileAsString(fileName):
    res = HttpRequestUtil.get(metaBaseEndpoint + "/getDomainFileAsString?fileName=" + fileName)
    return HttpRequestUtil.HttpResponseToString(res)


def getDomainFileAsMap(fileName):
    res = HttpRequestUtil.get(metaBaseEndpoint + "/getDomainFileAsMap?fileName=" + fileName)
    return Util.convertToDict(res)


def getDomainFileAsList(fileName):
    res = HttpRequestUtil.get(metaBaseEndpoint + "/getDomainFileAsList?fileName=" + fileName)
    return Util.convertToListOfDict(res)


def existsDomainFile(fileName):
    res = HttpRequestUtil.get(metaBaseEndpoint + "/getDomainFileAsList?fileName=" + fileName)
    return Util.convertToBool(res)


@multimethod(str)
def getKeyValue(key):
    return HttpRequestUtil.get(metaBaseEndpoint + "/getKeyValue?key=" + key)


@multimethod(str, str)
def getKeyValue(key, type):
    return HttpRequestUtil.get(metaBaseEndpoint + "/getKeyValue?key=" + key + "&type=" + type)


@multimethod(str, str, str, dict)
def makeClassFromData(className, tableName, pkAttrName, data):
    body = {
        "className": className,
        "tableName": tableName,
        "pkAttrName": pkAttrName,
        "data": data
    }
    return HttpRequestUtil.post(metaBaseEndpoint + "/makeClassFromData", body)


@multimethod(str, str, str, dict, dict)
def makeClassFromData(className, tableName, pkAttrName, data, attrTypeByNames):
    body = {
        "className": className,
        "tableName": tableName,
        "pkAttrName": pkAttrName,
        "data": data,
        "attrTypeByNames": attrTypeByNames
    }
    return HttpRequestUtil.post(metaBaseEndpoint + "/makeClassFromData", body)


@multimethod(str, str, str, dict, bool)
def makeClassFromData(className, tableName, pkAttrName, data, skipSaving):
    body = {
        "className": className,
        "tableName": tableName,
        "pkAttrName": pkAttrName,
        "data": data,
        "skipSaving": skipSaving
    }
    return HttpRequestUtil.post(metaBaseEndpoint + "/makeClassFromData", body)


@multimethod(str, str, str, dict, dict, bool)
def makeClassFromData(className, tableName, pkAttrName, data,
                      attrTypeByNames, skipSaving):
    body = {
        "className": className,
        "tableName": tableName,
        "pkAttrName": pkAttrName,
        "data": data,
        "attrTypeByNames": attrTypeByNames,
        "skipSaving": skipSaving
    }
    return HttpRequestUtil.post(metaBaseEndpoint + "/makeClassFromData", body)


@multimethod(str, str, str, dict, dict, bool, bool)
def makeClassFromData(className, tableName, pkAttrName, data,
                      attrTypeByNames, skipSaving, addSystemAttrs):
    body = {
        "className": className,
        "tableName": tableName,
        "pkAttrName": pkAttrName,
        "data": data,
        "attrTypeByNames": attrTypeByNames,
        "skipSaving": skipSaving,
        "addSystemAttrs": addSystemAttrs
    }
    return HttpRequestUtil.post(metaBaseEndpoint + "/makeClassFromData", body)


def makeLogicalClassFromData(className, data):
    body = {
        "className": className,
        "data": data
    }
    return HttpRequestUtil.post(metaBaseEndpoint + "/makeLogicalClassFromData", body)


@multimethod(str)
def getMetadata(id):
    return HttpRequestUtil.get(metaBaseEndpoint + "/getMetadata?id=" + id)


@multimethod(str, str, str)
def getMetadata(modelClassName, folder, name):
    return HttpRequestUtil.get(
        metaBaseEndpoint + "/getMetadata?modelClassName=" + modelClassName + "&folder=" + folder + "&name=" + name)


def saveMetadata(md):
    return HttpRequestUtil.post(metaBaseEndpoint + "/saveMetadata", md)


@multimethod(str)
def createFunctionSysTask(mdId):
    body = {
        "mdId": mdId
    }
    return HttpRequestUtil.post(metaBaseEndpoint + "/createFunctionSysTask", body)


@multimethod(str, str)
def createFunctionSysTask(orgName, name):
    body = {
        "orgName": orgName,
        "name": name
    }
    return HttpRequestUtil.post(metaBaseEndpoint + "/createFunctionSysTask", body)

