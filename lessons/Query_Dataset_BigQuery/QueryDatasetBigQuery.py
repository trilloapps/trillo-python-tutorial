from src.collager.pojo.ResultApi import Result
from src.collager.util import BigQueryApi


def getBQPage(parameters):
    if "query" not in parameters:
        return Result.getFailedResult("query is missing")
    query = str(parameters['query'])
    return BigQueryApi.getPage(query, 0, 10)

def getBqDatasetTables(parameters):
    return BigQueryApi.getBQTables(parameters["datasetName"])
