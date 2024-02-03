import base64

from src.collager.pojo.ResultApi import Result
from src.collager.util import StorageApi
from src.collager.util.LogApi import Log


def readFile(parameters):
    if "bucketName" not in parameters:
        return Result.getFailedResult("bucketName is missing")
    if "sourceFilePath" not in parameters:
        return Result.getFailedResult("sourceFilePath is missing")
    bucketName = str(parameters['bucketName'])
    sourceFilePath = str(parameters['sourceFilePath'])
    res = StorageApi.readFromBucket(bucketName, sourceFilePath)
    if res.isFailed():
        Log.error("Failed to read the file, error: " + res.getMessage())
        return res
    else:
        if isinstance(res.getData(), bytearray):
            byteArr = bytearray(res.getData())
        else:
            byteArr = (base64.b64decode(res.getData())).decode('utf-8')
        return Result.getSuccessResultWithData(byteArr)
