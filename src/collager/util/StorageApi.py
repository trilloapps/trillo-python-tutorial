from multimethods import multimethod

from src.collager.util.BaseApi import BaseApi
from src.collager.util.Util import Util
from src.collager.util.HttpRequestUtil import HttpRequestUtil
from src.io.util.Proxy import Proxy

storageBaseEndpoint = "/api/v1.1/storage"


def getFilePath(fileId):
    res = HttpRequestUtil.get(storageBaseEndpoint + "/getFilePath" + "/" + str(fileId))
    return HttpRequestUtil.HttpResponseToString(res)


def getFileIdByPath(absoluteFilePath):
    res = HttpRequestUtil.get(storageBaseEndpoint + "/getFileIdByPath/" + absoluteFilePath)
    strValue = HttpRequestUtil.HttpResponseToString(res)
    try:
        return int(strValue)
    except Exception as exc:
        return -1


def getFolderPath(folderId):
    res = HttpRequestUtil.get(storageBaseEndpoint + "/getFolderPath/" + folderId)
    return HttpRequestUtil.HttpResponseToString(res)


def getBucketName():
    res = HttpRequestUtil.get(storageBaseEndpoint + "/getBucketName")
    return HttpRequestUtil.HttpResponseToString(res)


@multimethod(str)
def getSignedUrl(filePath):
    res = Proxy.remoteCall("StorageApi", "getSignedUrl", filePath)
    return HttpRequestUtil.HttpResponseToString(res)


@multimethod(str, str, int, str)
def getSignedUrl(bucketName, filePath, duration, unit):
    res = Proxy.remoteCall("StorageApi", "getSignedUrl", bucketName, filePath, duration, unit)
    return HttpRequestUtil.HttpResponseToString(res)


@multimethod(str, str)
def getSignedUrl(bucketName, filePath):
    res = Proxy.remoteCall("StorageApi", "getSignedUrl", bucketName, filePath)
    return HttpRequestUtil.HttpResponseToString(res)


@multimethod(str, int, str)
def getSignedUrl(filePath, duration, unit):
    res = Proxy.remoteCall("StorageApi", "getSignedUrl", filePath, duration, unit)
    return HttpRequestUtil.HttpResponseToString(res)


def exists(filePath):
    res = HttpRequestUtil.get(storageBaseEndpoint + "/exists?filePath=" + filePath)
    return HttpRequestUtil.HttpResponseToBoolean(res)


@multimethod(str, str)
def copyFileWithinBucket(sourceFilePath, targetFilePath):
    body = {"sourceFilePath": sourceFilePath,
            "targetFilePath": targetFilePath}
    res = HttpRequestUtil.post(storageBaseEndpoint + "/copyFileWithinBucket", body)
    return Util.convertToResult(res)


@multimethod(str, str, bool)
def copyFileWithinBucket(sourceFilePath, targetFilePath, makePublic):
    body = {"sourceFilePath": sourceFilePath,
            "targetFilePath": targetFilePath,
            "makePublic": makePublic}
    res = HttpRequestUtil.post(storageBaseEndpoint + "/copyFileWithinBucket", body)
    return Util.convertToResult(res)


@multimethod(str, str, str)
def copyFileWithinBucket(bucketName, sourceFilePath, targetFilePath):
    body = {"sourceFilePath": sourceFilePath,
            "targetFilePath": targetFilePath,
            "bucketName": bucketName}
    res = HttpRequestUtil.post(storageBaseEndpoint + "/copyFileWithinBucket", body)
    return Util.convertToResult(res)


@multimethod(str, str, str, bool)
def copyFileWithinBucket(bucketName, sourceFilePath, targetFilePath, makePublic):
    body = {"sourceFilePath": sourceFilePath,
            "targetFilePath": targetFilePath,
            "bucketName": bucketName,
            "makePublic": makePublic}
    res = HttpRequestUtil.post(storageBaseEndpoint + "/copyFileWithinBucket", body)
    return Util.convertToResult(res)


@multimethod(str, str)
def copyFileToBucket(sourceFilePath, targetFilePath):
    body = {"sourceFilePath": sourceFilePath,
            "targetFilePath": targetFilePath}
    res = HttpRequestUtil.post(storageBaseEndpoint + "/copyFileToBucket", body)
    return Util.convertToResult(res)


@multimethod(str, str, str)
def copyFileToBucket(bucketName, sourceFilePath, targetFilePath):
    body = {"sourceFilePath": sourceFilePath,
            "targetFilePath": targetFilePath,
            "bucketName": bucketName}
    res = HttpRequestUtil.post(storageBaseEndpoint + "/copyFileToBucket", body)
    return Util.convertToResult(res)


@multimethod(str, str, str, str)
def copyFileToBucket(bucketName, serviceAccountPropName, sourceFilePath, targetFilePath):
    body = {"sourceFilePath": sourceFilePath,
            "targetFilePath": targetFilePath,
            "bucketName": bucketName,
            "serviceAccountPropName": serviceAccountPropName}
    res = HttpRequestUtil.post(storageBaseEndpoint + "/copyFileToBucket", body)
    return Util.convertToResult(res)


@multimethod(str, str)
def copyFileFromBucket(sourceFilePath, targetFilePath):
    body = {"sourceFilePath": sourceFilePath,
            "targetFilePath": targetFilePath}
    res = HttpRequestUtil.post(storageBaseEndpoint + "/copyFileFromBucket", body)
    return Util.convertToResult(res)


@multimethod(str, str, str)
def copyFileFromBucket(bucketName, sourceFilePath, targetFilePath):
    body = {"sourceFilePath": sourceFilePath,
            "targetFilePath": targetFilePath,
            "bucketName": bucketName}
    res = HttpRequestUtil.post(storageBaseEndpoint + "/copyFileFromBucket", body)
    return Util.convertToResult(res)


@multimethod(str, str, str, str)
def copyFileFromBucket(bucketName, serviceAccountPropName, sourceFilePath, targetFilePath):
    body = {"sourceFilePath": sourceFilePath,
            "targetFilePath": targetFilePath,
            "bucketName": bucketName,
            "serviceAccountPropName": serviceAccountPropName}
    res = HttpRequestUtil.post(storageBaseEndpoint + "/copyFileFromBucket", body)
    return Util.convertToResult(res)


@multimethod(str)
def readFromBucket(sourceFilePath):
    body = {"sourceFilePath": sourceFilePath}
    res = HttpRequestUtil.post(storageBaseEndpoint + "/readFromBucket", body)
    return Util.convertToResult(res)


@multimethod(str, str)
def readFromBucket(bucketName, sourceFilePath):
    body = {"sourceFilePath": sourceFilePath,
            "bucketName": bucketName}
    res = HttpRequestUtil.post(storageBaseEndpoint + "/readFromBucket", body)
    return Util.convertToResult(res)


@multimethod(str, bool)
def listFiles(pathName, versioned):
    body = {"pathName": pathName,
            "versioned": versioned}
    res = HttpRequestUtil.post(storageBaseEndpoint + "/listFiles", body)
    return Util.convertToListOfDict(res)


@multimethod(str, str, bool)
def listFiles(bucketName, pathName, versioned):
    body = {"bucketName": bucketName,
            "pathName": pathName,
            "versioned": versioned}
    res = HttpRequestUtil.post(storageBaseEndpoint + "/listFiles", body)
    return Util.convertToListOfDict(res)


@multimethod(str, str, bool)
def getFilesPage(bucketName, pathName, versioned):
    body = {"bucketName": bucketName,
            "pathName": pathName,
            "versioned": versioned}
    return HttpRequestUtil.post(storageBaseEndpoint + "/getFilesPage", body)


@multimethod(str, str, bool, str, int)
def getFilesPage(bucketName, pathName, versioned, pageToken, pageSize):
    body = {"bucketName": bucketName,
            "pathName": pathName,
            "versioned": versioned}
    return HttpRequestUtil.post(storageBaseEndpoint + "/getFilesPage", body)


@multimethod(str, bytes, str, str)
def writeToBucket(bucketName, bytes, targetFilePath, contentType):
    return BaseApi.remoteCallAsResult("StorageApi", "writeToBucket", bucketName, bytes, targetFilePath, contentType)


@multimethod(bytes, str, str)
def writeToBucket(bytes, targetFilePath, contentType):
    return BaseApi.remoteCallAsResult("StorageApi", "writeToBucket", bytes, targetFilePath, contentType)


def saveFileObject(fileObject):
    body = {"fileObject": fileObject},
    return HttpRequestUtil.post(storageBaseEndpoint + "/saveFileObject", body)


def shareWithTenants(params):
    body = {"params": params},
    return HttpRequestUtil.post(storageBaseEndpoint + "/shareWithTenants", body)


@multimethod(str, str)
def copyLargeFileToBucket(sourceFilePath, targetFilePath):
    body = {"sourceFilePath": sourceFilePath,
            "targetFilePath": targetFilePath}
    res = HttpRequestUtil.post(storageBaseEndpoint + "/copyLargeFileToBucket", body)
    return Util.convertToResult(res)


@multimethod(str, str, str)
def copyLargeFileToBucket(bucketName, sourceFilePath, targetFilePath):
    body = {"sourceFilePath": sourceFilePath,
            "targetFilePath": targetFilePath,
            "bucketName": bucketName}
    res = HttpRequestUtil.post(storageBaseEndpoint + "/copyLargeFileToBucket", body)
    return Util.convertToResult(res)


@multimethod(str, str, str, str)
def copyLargeFileToBucket(bucketName, serviceAccountPropName, sourceFilePath, targetFilePath):
    body = {"sourceFilePath": sourceFilePath,
            "targetFilePath": targetFilePath,
            "bucketName": bucketName,
            "serviceAccountPropName": serviceAccountPropName}
    res = HttpRequestUtil.post(storageBaseEndpoint + "/copyLargeFileToBucket", body)
    return Util.convertToResult(res)


@multimethod(str, str)
def makePublic(bucketName, filePath):
    body = {"filePath": filePath,
            "bucketName": bucketName}
    res = HttpRequestUtil.post(storageBaseEndpoint + "/makePublic", body)
    return Util.convertToResult(res)


@multimethod(str, str, str)
def makePublic(bucketName, serviceAccountPropName, filePath):
    body = {"filePath": filePath,
            "bucketName": bucketName,
            "serviceAccountPropName": serviceAccountPropName}
    res = HttpRequestUtil.post(storageBaseEndpoint + "/makePublic", body)
    return Util.convertToResult(res)
