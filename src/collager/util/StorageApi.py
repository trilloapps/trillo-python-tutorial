import json

import requests
from multimethods import multimethod

from src.collager.pojo.ResultApi import Result
from src.collager.util import HttpUtil
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
    return BaseApi.remoteCall("StorageApi", "copyFileWithinBucket", sourceFilePath, targetFilePath)


@multimethod(str, str, bool)
def copyFileWithinBucket(sourceFilePath, targetFilePath, makePublic):
    return BaseApi.remoteCall("StorageApi", "copyFileWithinBucket", sourceFilePath, targetFilePath, makePublic)


@multimethod(str, str, str)
def copyFileWithinBucket(bucketName, sourceFilePath, targetFilePath):
    return BaseApi.remoteCall("StorageApi", "copyFileWithinBucket", bucketName, sourceFilePath, targetFilePath)


@multimethod(str, str, str, bool)
def copyFileWithinBucket(bucketName, sourceFilePath, targetFilePath, makePublic):
    return BaseApi.remoteCall("StorageApi", "copyFileWithinBucket", bucketName, sourceFilePath, targetFilePath, makePublic)


@multimethod(str, str)
def copyFileToBucket(sourceFilePath, targetFilePath):
    return BaseApi.remoteCall("StorageApi", "copyFileToBucket", sourceFilePath, targetFilePath)


@multimethod(str, str, str)
def copyFileToBucket(bucketName, sourceFilePath, targetFilePath):
    return BaseApi.remoteCall("StorageApi", "copyFileToBucket", bucketName, sourceFilePath, targetFilePath)


@multimethod(str, str, str, str)
def copyFileToBucket(bucketName, serviceAccountPropName, sourceFilePath, targetFilePath):
    return BaseApi.remoteCall("StorageApi", "copyFileToBucket", bucketName, serviceAccountPropName, sourceFilePath, targetFilePath)


@multimethod(str, str)
def copyFileFromBucket(sourceFilePath, targetFilePath):
    return BaseApi.remoteCall("StorageApi", "copyFileFromBucket", sourceFilePath, targetFilePath)


@multimethod(str, str, str)
def copyFileFromBucket(bucketName, sourceFilePath, targetFilePath):
    return BaseApi.remoteCall("StorageApi", "copyFileFromBucket", bucketName, sourceFilePath, targetFilePath)


@multimethod(str, str, str, str)
def copyFileFromBucket(bucketName, serviceAccountPropName, sourceFilePath, targetFilePath):
    return BaseApi.remoteCall("StorageApi", "copyFileFromBucket", bucketName, serviceAccountPropName, sourceFilePath, targetFilePath)


@multimethod(str)
def readFromBucket(sourceFilePath):
    return BaseApi.remoteCall("StorageApi", "readFromBucket", sourceFilePath)


@multimethod(str, str)
def readFromBucket(bucketName, sourceFilePath):
    return BaseApi.remoteCall("StorageApi", "readFromBucket", bucketName, sourceFilePath)


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


@multimethod(str, str, str, str)
def writeToBucket(bucketName, base64Str, targetFilePath, contentType):
    body = {"bucketName": bucketName,
            "base64Str": base64Str,
            "targetFilePath": targetFilePath,
            "contentType": contentType}
    return HttpRequestUtil.post(storageBaseEndpoint + "/writeToBucket", body)


@multimethod(str, str, str)
def writeToBucket(base64Str, targetFilePath, contentType):
    body = {"base64Str": base64Str,
            "targetFilePath": targetFilePath,
            "contentType": contentType}
    return HttpRequestUtil.post(storageBaseEndpoint + "/writeToBucket", body)


def saveFileObject(fileObject):
    body = {"fileObject": fileObject},
    return HttpRequestUtil.post(storageBaseEndpoint + "/saveFileObject", body)


def shareWithTenants(params):
    body = {"params": params},
    return HttpRequestUtil.post(storageBaseEndpoint + "/shareWithTenants", body)


@multimethod(str, str)
def copyLargeFileToBucket(sourceFilePath, targetFilePath):
    return uploadFile(Proxy.getServerUrl() + "/ds/copyFileToBucket", "", None, sourceFilePath,
                      targetFilePath)


@multimethod(str, str, str)
def copyLargeFileToBucket(bucketName, sourceFilePath, targetFilePath):
    return uploadFile(Proxy.getServerUrl() + "/ds/copyFileToBucket", bucketName, None, sourceFilePath,
                      targetFilePath)


@multimethod(str, str, str, str)
def copyLargeFileToBucket(bucketName, serviceAccountPropName, sourceFilePath, targetFilePath):
    return uploadFile(Proxy.getServerUrl() + "/ds/copyFileToBucket", bucketName, serviceAccountPropName , sourceFilePath, targetFilePath)

def uploadFile(url, bucketName, serviceAccountPropName, sourceFilePath, targetFilePath):
    try:
        headers = {
            "Authorization": "Bearer " + Proxy.getAccessToken(),
            "x-org-name": Proxy.getOrgName(),
            "x-app-name": Proxy.getAppName()
        }

        files = {
            'file': open(sourceFilePath, 'rb'),
            'bucketName': (None, bucketName),
            'targetFilePath': (None, targetFilePath)
        }

        if serviceAccountPropName is not None:
            files['serviceAccountPropName'] = (None, serviceAccountPropName)

        response = requests.post(url, headers=headers, files=files)

        if response.status_code == 200:
            return Result.getSuccessResultWithData(response.text)
        else:
            if response.content:
                try:
                    content = response.content.decode('utf-8')
                    data = json.loads(content)
                    if "_rtag" in data:
                        result = Result(data)
                        return result
                    return Result.getFailedResult(
                        "Invalid response received, HTTP code: " + str(response.status_code) + "\n" + content)
                except Exception as exc:
                    pass
                return Result.getFailedResult("Invalid response received, HTTP code: " + str(response.status_code))
            else:
                return Result.getFailedResult("No response received, HTTP code: " + str(response.status_code))
    except Exception as exc:
        return Result.getFailedResult(str(exc))


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


def deleteFileFromBucket(bucketName, sourceFilePath):
    return BaseApi.remoteCallAsResult("StorageApi", "deleteFileFromBucket", bucketName, sourceFilePath)

