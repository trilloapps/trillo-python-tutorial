from src.collager.pojo.ResultApi import Result
from src.collager.util import StorageApi


def generate(parameters):
    if "bucketName" not in parameters:
        return Result.getFailedResult("bucketName is missing")
    if "sourceFilePath" not in parameters:
        return Result.getFailedResult("sourceFilePath is missing")
    bucketName = parameters["bucketName"]
    sourceFilePath = parameters["sourceFilePath"]
    return StorageApi.getSignedUrl(bucketName, sourceFilePath)

