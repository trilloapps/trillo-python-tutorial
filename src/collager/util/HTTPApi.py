from typing import List, Dict, Union
from multimethods import multimethod
from src.collager.util.BaseApi import BaseApi


@multimethod(str)
def get(requestUrl):
    return BaseApi.remoteCallAsResult("HttpApi", "get", requestUrl)


@multimethod(str)
def get2(requestUrl):
    return BaseApi.remoteCallAsResult("HttpApi", "get2", requestUrl)


@multimethod(str, dict)
def get(requestUrl, headers):
    return BaseApi.remoteCallAsResult("HttpApi", "get", requestUrl, headers)


@multimethod(str, dict, int, int)
def get(requestUrl, headers, retryCount, waitTime):
    return BaseApi.remoteCallAsResult("HttpApi", "get", requestUrl, headers, retryCount, waitTime)


@multimethod(str, object)
def post(requestUrl, body):
    return BaseApi.remoteCallAsResult("HttpApi", "post", requestUrl, body)


@multimethod(str, object, dict)
def post(requestUrl, body, headers):
    return BaseApi.remoteCallAsResult("HttpApi", "post", requestUrl, body, headers)


@multimethod(str, dict, dict)
def postFormData(requestUrl, body, headers):
    return BaseApi.remoteCallAsResult("HttpApi", "postFormData", requestUrl, body, headers)


@multimethod(str, dict, dict)
def postFormDataAsString(requestUrl, body, headers):
    return BaseApi.remoteCallAsResult("HttpApi", "postFormDataAsString", requestUrl, body, headers)


@multimethod(str, object)
def put(requestUrl, body):
    return BaseApi.remoteCallAsResult("HttpApi", "put", requestUrl, body, None)


@multimethod(str, object, dict)
def put(requestUrl, body, headers):
    return BaseApi.remoteCallAsResult("HttpApi", "put", requestUrl, body, headers)


@multimethod(str, object)
def patch(requestUrl, body):
    return BaseApi.remoteCallAsResult("HttpApi", "patch", requestUrl, body, None)


@multimethod(str, object, dict)
def patch(requestUrl, body, headers):
    return BaseApi.remoteCallAsResult("HttpApi", "patch", requestUrl, body, headers)


@multimethod(str, object)
def delete(requestUrl, body):
    return BaseApi.remoteCallAsResult("HttpApi", "delete", requestUrl, body)


@multimethod(str, object, dict)
def delete(requestUrl, body, headers):
    return BaseApi.remoteCallAsResult("HttpApi", "delete", requestUrl, body, headers)


@multimethod(str, str)
def getAsString(requestUrl, contentType):
    return BaseApi.remoteCallAsResult("HttpApi", "getAsString", requestUrl, contentType)


@multimethod(str, str, dict)
def getAsString(requestUrl, contentType, headers):
    return BaseApi.remoteCallAsResult("HttpApi", "getAsString", requestUrl, contentType, headers)
