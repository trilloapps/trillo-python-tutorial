from src.collager.util.BaseApi import BaseApi
from src.collager.util.Util import Util
from src.collager.util.HttpRequestUtil import HttpRequestUtil

umBaseEndpoint = "/api/v1.1/userAuth"


def signup(userMap):
    res = HttpRequestUtil.post(umBaseEndpoint + "/user/signup", userMap)
    return Util.convertToResult(res)


def resetPassword(user):
    res = HttpRequestUtil.post(umBaseEndpoint + "/user/resetPassword", user)
    return Util.convertToResult(res)


def setPassword(user):
    res = HttpRequestUtil.post(umBaseEndpoint + "/user/setPassword", user)
    return Util.convertToResult(res)


def forgotPassword(forgotPassword):
    res = HttpRequestUtil.post(umBaseEndpoint + "/user/forgotPassword", forgotPassword)
    return Util.convertToResult(res)


def sendOneTimePin(params):
    return HttpRequestUtil.post(umBaseEndpoint + "/user/sendOneTimePin", params)


def verifyOneTimePin(params):
    res = HttpRequestUtil.post(umBaseEndpoint + "/user/verifyOneTimePin", params)
    return Util.convertToResult(res)


def sendOneTimeCodeByEmail(params):
    res = HttpRequestUtil.post(umBaseEndpoint + "/user/sendOneTimeCodeByEmail", params)
    return Util.convertToResult(res)


def resendVerifyEmail(params):
    res = HttpRequestUtil.post(umBaseEndpoint + "/user/resendVerifyEmail", params)
    return Util.convertToResult(res)


def viaemail(action, parameter, orgName):
    return BaseApi.remoteCall("UserAuthApi", "viaemail", action, parameter, orgName)


def getUserByEmailKey(key):
    return BaseApi.remoteCall("UserAuthApi", "getUserByEmailKey", key)
