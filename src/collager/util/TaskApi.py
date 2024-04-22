from typing import Any, Dict
from src.collager.pojo.ResultApi import Result
from src.collager.util.BaseApi import BaseApi


class TaskApi():

    @staticmethod
    def isMyTaskCancelled() -> bool:
        return False  # return trivially false for local testing

    @staticmethod
    def getTaskId() -> int:
        return -1

    @staticmethod
    def cancelRemoteRequest(requestId: str) -> None:
        return

    @staticmethod
    def enqueueSvcRequest(queueId: str, svcUrl: str, svcToken: str,
                          serviceName: str, callbackFunctionName: str, methodName: str,
                          serviceRequestBody: Dict[str, Any], context: Dict[str, Any]) -> Result:
        return BaseApi.remoteCallAsResult("TaskApi", "enqueueSvcRequest", queueId, svcUrl, svcToken,
                                          serviceName, callbackFunctionName, methodName,
                                          serviceRequestBody, context)
