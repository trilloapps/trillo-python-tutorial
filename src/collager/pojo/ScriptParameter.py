from typing import Dict

from src.io.util.Proxy import Proxy


class ScriptParameter:
    def __init__(self):
        super().__init__()

    @classmethod
    def makeScriptParameter(cls, inputData, stateMap=None, taskName=None, executionId=-1):
        p = ScriptParameter()
        p.setV(inputData)
        if stateMap:
            p.update(stateMap)
        p.setTaskName(taskName)
        p.setExecutionId(executionId)
        loginResponse = Proxy.getLoginResponse()

        user = loginResponse.get("user")
        if isinstance(user, dict):
            p.idOfUser = user.get("id", -1)
            p.userId = user.get("userId", "")
            p.firstName = user.get("firstName", "")
            p.lastName = user.get("lastName", "")
            p.email = user.get("email", "")
            p.userOrgName = user.get("orgName", "")
            p.externalId = user.get("externalId", "")
            p.role = user.get("role", "")
            p.emailVerified = bool(user.get("emailVerified", ""))
            p.tenantId = user.get("tenantId", "")
            p.tenantName = user.get("tenantName", "")
            p.userOrgId = user.get("orgId", -1)

        p.appName = Proxy.getAppName()
        p.orgName = Proxy.getOrgName()
        return p
