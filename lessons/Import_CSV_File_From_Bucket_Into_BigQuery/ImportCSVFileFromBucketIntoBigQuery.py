from src.collager.pojo.ResultApi import Result
from src.collager.util import BigQueryApi
from src.collager.util.api import Api

@Api(httpMethod="post")
def importCSV(parameters):
    if "datasetName" not in parameters:
        return Result.getFailedResult("datasetName is missing")
    if "tableName" not in parameters:
        return Result.getFailedResult("tableName is missing")
    if "sourceUri" not in parameters:
        return Result.getFailedResult("sourceUri is missing")
    if "schema" not in parameters:
        return Result.getFailedResult("schema is missing")
    datasetName = str(parameters['datasetName'])
    tableName = str(parameters['tableName'])
    sourceUri = str(parameters['sourceUri'])
    schema = list(parameters['schema'])
    numberOfRowsToSkip = 1
    res = BigQueryApi.importCSVbyURIIntoTable(datasetName, tableName, sourceUri, schema, numberOfRowsToSkip)
    if res.isSuccess():
        return Result.getSuccessResultWithMsg("Successfully loaded data")
    return res
