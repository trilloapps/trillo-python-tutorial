from src.collager.pojo.ResultApi import Result
from src.collager.util import BigQueryApi
from src.collager.util.api import Api

@Api(httpMethod="post")
def getBQPage(parameters):
    if "query" not in parameters:
        return Result.getFailedResult("query is missing")
    return BigQueryApi.getPage(parameters["query"], 0, 10)
