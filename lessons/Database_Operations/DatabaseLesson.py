from src.collager.pojo.ResultApi import Result
from src.collager.util import DSApi

from src.collager.util.api import Api


@Api(httpMethod="get")
def queryRecordsFromDSById(parameters):
    if "id" not in parameters:
        return Result.getFailedResult("id is missing")
    if "tableName" not in parameters:
        return Result.getFailedResult("tableName is missing")

    id = parameters["id"]
    tableName = parameters["tableName"]
    return DSApi.get("shared.common." + tableName, id)


@Api(httpMethod="post")
def saveManyRecordsInDs(parameters):
    if "records" not in parameters:
        return Result.getFailedResult("records is missing")

    records = list(parameters["records"])
    tableName = parameters["tableName"]
    return DSApi.saveManyIgnoreError("shared.common." + tableName, records)


@Api(httpMethod="post")
def updateRecordInDs(parameters):
    if "updateAttributes" not in parameters:
        return Result.getFailedResult("updateAttributes is missing")
    if "id" not in parameters:
        return Result.getFailedResult("id is missing")
    if "tableName" not in parameters:
        return Result.getFailedResult("tableName is missing")

    updateAttributes = dict(parameters["updateAttributes"])
    tableName = parameters["tableName"]
    id = str(parameters["id"])
    return DSApi.updateUsingMap("shared.common." + tableName, id, updateAttributes)
