from src.collager.util.HttpRequestUtil import HttpRequestUtil
from src.collager.util.Util import Util

commandBaseEndpoint = "/api/v1.1/command"


def runOSCmd(argList):
    body = {"argList": argList}
    res = HttpRequestUtil.post(commandBaseEndpoint + "/runOSCmd", body)
    return Util.convertToResult(res)
