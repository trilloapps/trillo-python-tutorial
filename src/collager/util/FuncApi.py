from multimethods import multimethod
from src.collager.util.Util import Util
from src.collager.util.HttpRequestUtil import HttpRequestUtil
from src.io.util.Proxy import Proxy

functionBaseEndpoint = "/api/v1.1/func"


@multimethod(str, dict)
def executeFunction(functionName, params):
    body = {
        "params": params
    }
    res = HttpRequestUtil.post(functionBaseEndpoint + "/executeFunction/" + functionName, body)
    return Util.convertToResult(res)


@multimethod(str, str, dict)
def executeFunction(appName, functionName, params):
    body = {
        "appName": appName,
        "params": params
    }
    res = HttpRequestUtil.post(functionBaseEndpoint + "/executeFunction/" + functionName, body)
    return Util.convertToResult(res)


@multimethod(str, str, str, dict, bool)
def executeFunction(appName, functionName, methodName, params, preAuthCall):
    body = {
        "appName": appName,
        "methodName": methodName,
        "params": params,
        "preAuthCall": preAuthCall
    }
    res = HttpRequestUtil.post(functionBaseEndpoint + "/executeFunction/" + functionName, body)
    return Util.convertToResult(res)


@multimethod(str, str, str, dict)
def executeFunctionWithMethod(appName, functionName, methodName, params):
    body = {
        "appName": appName,
        "methodName": methodName,
        "params": params
    }
    res = HttpRequestUtil.post(functionBaseEndpoint + "/executeFunctionWithMethod/" + functionName, body)
    return Util.convertToResult(res)


@multimethod(str, str, dict)
def executeFunctionWithMethod(functionName, methodName, params):
    body = {
        "methodName": methodName,
        "params": params
    }
    res = HttpRequestUtil.post(functionBaseEndpoint + "/executeFunctionWithMethod/" + functionName, body)
    return Util.convertToResult(res)


@multimethod(str, str, str, dict)
def createTask(taskName, taskType, functionName, params):
    body = {
        "taskName": taskName,
        "taskType": taskType,
        "params": params
    }

    res = HttpRequestUtil.post(functionBaseEndpoint + "/createTask/" + functionName, body)
    return Util.convertToResult(res)


@multimethod(str, str, str, str, dict)
def createTask(taskName, taskType, appName, functionName, params):
    body = {
        "taskName": taskName,
        "taskType": taskType,
        "appName": appName,
        "params": params
    }

    res = HttpRequestUtil.post(functionBaseEndpoint + "/createTask/" + functionName, body)
    return Util.convertToResult(res)


@multimethod(str, str, str, str, str, dict)
def createTask2(taskName, taskType, appName, functionName, methodName, params):
    body = {
        "taskName": taskName,
        "taskType": taskType,
        "appName": appName,
        "methodName": methodName,
        "params": params
    }

    res = HttpRequestUtil.post(functionBaseEndpoint + "/createTask2/" + functionName, body)
    return Util.convertToResult(res)


@multimethod(str, str, str, str, dict)
def createTask2(taskName, taskType, functionName, methodName, params):
    body = {
        "taskName": taskName,
        "taskType": taskType,
        "methodName": methodName,
        "params": params
    }

    res = HttpRequestUtil.post(functionBaseEndpoint + "/createTask2/" + functionName, body)
    return Util.convertToResult(res)


@multimethod(str, str, str, str, bool, dict)
def createTask2(taskName, taskType, functionName, methodName, inbuilt, params):
    body = {
        "taskName": taskName,
        "taskType": taskType,
        "methodName": methodName,
        "inbuilt": inbuilt,
        "params": params
    }

    res = HttpRequestUtil.post(functionBaseEndpoint + "/createTask2/" + functionName, body)
    return Util.convertToResult(res)


@multimethod(str, str, str, str, str, bool, dict)
def createTask2(taskName, taskType, appName, functionName, methodName, inbuilt, params):
    body = {
        "taskName": taskName,
        "taskType": taskType,
        "appName": appName,
        "methodName": methodName,
        "inbuilt": inbuilt,
        "params": params
    }

    res = HttpRequestUtil.post(functionBaseEndpoint + "/createTask2/" + functionName, body)
    return Util.convertToResult(res)


@multimethod(str, str, str, str, dict)
def createTaskBySourceUid(taskName, taskType, sourceUid, functionName, params):
    body = {
        "taskName": taskName,
        "taskType": taskType,
        "sourceUid": sourceUid,
        "params": params
    }

    res = HttpRequestUtil.post(functionBaseEndpoint + "/createTaskBySourceUid/" + functionName, body)
    return Util.convertToResult(res)


@multimethod(str, str, str, str, str, dict)
def createTaskBySourceUid(taskName, taskType, sourceUid, appName, functionName, params):
    body = {
        "taskName": taskName,
        "taskType": taskType,
        "sourceUid": sourceUid,
        "appName": appName,
        "params": params
    }

    res = HttpRequestUtil.post(functionBaseEndpoint + "/createTaskBySourceUid/" + functionName, body)
    return Util.convertToResult(res)


@multimethod(str, str, str, str, str, str, dict)
def createTaskBySourceUid2(taskName, taskType, sourceUid, appName, functionName, methodName, params):
    body = {
        "taskName": taskName,
        "taskType": taskType,
        "sourceUid": sourceUid,
        "appName": appName,
        "methodName": methodName,
        "params": params
    }

    res = HttpRequestUtil.post(functionBaseEndpoint + "/createTaskBySourceUid2/" + functionName, body)
    return Util.convertToResult(res)


@multimethod(str, str, str, str, str, dict)
def createTaskBySourceUid2(taskName, taskType, sourceUid, functionName, methodName, params):
    body = {
        "taskName": taskName,
        "taskType": taskType,
        "sourceUid": sourceUid,
        "methodName": methodName,
        "params": params
    }

    res = HttpRequestUtil.post(functionBaseEndpoint + "/createTaskBySourceUid2/" + functionName, body)
    return Util.convertToResult(res)


@multimethod(str, str, str, str, str, bool, dict)
def createTaskBySourceUid2(taskName, taskType, sourceUid, functionName, methodName, inbuilt, params):
    body = {
        "taskName": taskName,
        "taskType": taskType,
        "sourceUid": sourceUid,
        "methodName": methodName,
        "inbuilt": inbuilt,
        "params": params
    }

    res = HttpRequestUtil.post(functionBaseEndpoint + "/createTaskBySourceUid2/" + functionName, body)
    return Util.convertToResult(res)


@multimethod(str, str, str, str, str, str, bool, dict)
def createTaskBySourceUid2(taskName, taskType, sourceUid, appName, functionName, methodName, inbuilt, params):
    body = {
        "taskName": taskName,
        "taskType": taskType,
        "appName": appName,
        "sourceUid": sourceUid,
        "methodName": methodName,
        "inbuilt": inbuilt,
        "params": params
    }

    res = HttpRequestUtil.post(functionBaseEndpoint + "/createTaskBySourceUid2/" + functionName, body)
    return Util.convertToResult(res)


@multimethod(str, str)
def executeSSH(hostName, command):
    body = {
        "hostName": hostName,
        "command": command
    }

    res = HttpRequestUtil.post(functionBaseEndpoint + "/executeSSH", body)
    return Util.convertToResult(res)


@multimethod(str, str, bool)
def executeSSH(hostName, command, asyncBol):
    body = {
        "hostName": hostName,
        "command": command,
        "async": asyncBol
    }

    res = HttpRequestUtil.post(functionBaseEndpoint + "/executeSSH", body)
    return Util.convertToResult(res)


@multimethod(str, bool)
def executeSSH(command, asyncBol):
    body = {

        "command": command,
        "async": asyncBol
    }

    res = HttpRequestUtil.post(functionBaseEndpoint + "/executeSSH", body)
    return Util.convertToResult(res)


def pingTask():
    return HttpRequestUtil.get(functionBaseEndpoint + "/pingTask")


def createFunctionSysTask(taskName, taskType, appName, functionName, functionParams):
    body = {
        "taskName": taskName,
        "taskType": taskType,
        "appName": appName,
        "functionParams": functionParams
    }

    res = HttpRequestUtil.post(functionBaseEndpoint + "/createFunctionSysTask/" + functionName, body)
    return Util.convertToResult(res)
