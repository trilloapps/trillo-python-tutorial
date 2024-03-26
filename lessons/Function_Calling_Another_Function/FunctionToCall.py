from src.collager.pojo.ResultApi import Result
from src.collager.util import DSApi

from src.collager.util.api import Api


@Api(httpMethod="post")
def queryRecordsFromDSById(parameters):
    if "id" not in parameters:
        return Result.getFailedResult("id is missing")
    if "tableName" not in parameters:
        return Result.getFailedResult("tableName is missing")

    id = parameters["id"]
    tableName = parameters["tableName"]
    return DSApi.get("shared.common." + tableName, id)


def saveManyRecordsInDs(parameters):
    if "records" not in parameters:
        return Result.getFailedResult("records is missing")

    records = list(parameters["records"])
    tableName = parameters["tableName"]
    return DSApi.saveManyMapListIgnoreError("shared.common." + tableName, records)
