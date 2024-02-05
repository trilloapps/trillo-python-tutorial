from uuid import UUID

from src.collager.pojo.ResultApi import Result
from src.collager.util import FuncApi, LogApi


def saveAndQueryRecordInDS(parameters):
    resForQuery = FuncApi.executeFunctionWithMethod("FunctionToCall", "queryRecordsFromDSById", parameters)
    if resForQuery.isSuccess():
        LogApi.auditLogInfo(resForQuery.getData().toString())
        taskName = "sampleTask"
        taskType = "background"
        sourceUid = UUID.randomUUID().toString()
        functionName = "FunctionToCall"
        methodName = "queryRecordsFromDSById"
        resSave = FuncApi.createTaskBySourceUid2(taskName, taskType, sourceUid, functionName, methodName, parameters)
        return resSave
    return resForQuery
