from multimethods import multimethod
from src.collager.util.HttpRequestUtil import HttpRequestUtil

gcsBaseEndpoint = "/api/v1.1/gcs"


def getTrilloGCSBucket():
    res = HttpRequestUtil.get(gcsBaseEndpoint + "/getTrilloGCSBucket")
    return HttpRequestUtil.HttpResponseToString(res)


def getTrilloGCSBucketURI():
    res = HttpRequestUtil.get(gcsBaseEndpoint + "/getTrilloGCSBucketURI")
    return HttpRequestUtil.HttpResponseToString(res)


@multimethod(str)
def getGCSFileURI(pathToFile):
    res = HttpRequestUtil.get(gcsBaseEndpoint + "/getGCSFileURI?pathToFile=" + pathToFile)
    return HttpRequestUtil.HttpResponseToString(res)


@multimethod(str, str)
def getGCSFileURI(path, fileName):
    res = HttpRequestUtil.get(gcsBaseEndpoint + "/getGCSFileURI?path=" + path + "&fileName=" + fileName)
    return HttpRequestUtil.HttpResponseToString(res)


def getLocalPath(bucketPath):
    res = HttpRequestUtil.get(gcsBaseEndpoint + "/getLocalPath?bucketPath=" + bucketPath)
    return HttpRequestUtil.HttpResponseToString(res)


def getGCSPath(appDataPath):
    res = HttpRequestUtil.get(gcsBaseEndpoint + "/getGCSPath?appDataPath=" + appDataPath)
    return HttpRequestUtil.HttpResponseToString(res)


def getGCSTempPath():
    res = HttpRequestUtil.get(gcsBaseEndpoint + "/getGCSTempPath")
    return HttpRequestUtil.HttpResponseToString(res)


def getDefaultRootFolder():
    res = HttpRequestUtil.get(gcsBaseEndpoint + "/getDefaultRootFolder")
    return HttpRequestUtil.HttpResponseToString(res)
