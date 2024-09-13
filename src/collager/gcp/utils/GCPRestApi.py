from src.collager.util.BaseApi import BaseApi
from multimethods import multimethod


@multimethod(str)
def get(requestUrl):
    return BaseApi.remoteCall("GCPRestApi", "get", requestUrl)


@multimethod(str, dict)
def post(requestUrl, body):
    return BaseApi.remoteCall("GCPRestApi", "post", requestUrl, body)


@multimethod(str, dict, dict)
def post(requestUrl, body, headers):
    return BaseApi.remoteCall("GCPRestApi", "post", requestUrl, body, headers)


@multimethod(str, dict)
def put(requestUrl, body):
    return BaseApi.remoteCall("GCPRestApi", "put", requestUrl, body)


@multimethod(str, dict)
def patch(requestUrl, body):
    return BaseApi.remoteCall("GCPRestApi", "patch", requestUrl, body)


@multimethod(str, dict)
def delete(requestUrl, body):
    return BaseApi.remoteCall("GCPRestApi", "delete", requestUrl, body)


@multimethod(str, str, str)
def get(requestUrl, serviceAccountKeyPropName, authenticationPath):
    return BaseApi.remoteCall("GCPRestApi", "get", requestUrl,
                              serviceAccountKeyPropName,
                              authenticationPath)


@multimethod(str, dict, str, str)
def post(requestUrl, body, serviceAccountKeyPropName, authenticationPath):
    return BaseApi.remoteCall("GCPRestApi", "post", requestUrl, body,
                              serviceAccountKeyPropName, authenticationPath)


@multimethod(str, dict, dict, str, str)
def post(requestUrl, body, headers, serviceAccountKeyPropName, authenticationPath):
    return BaseApi.remoteCall("GCPRestApi", "post", requestUrl, body, headers,
                              serviceAccountKeyPropName, authenticationPath)


@multimethod(str, dict, str, str)
def put(requestUrl, body, serviceAccountKeyPropName, authenticationPath):
    return BaseApi.remoteCall("GCPRestApi", "put", requestUrl, body,
                              serviceAccountKeyPropName, authenticationPath)


@multimethod(str, dict, str, str)
def patch(requestUrl, body, serviceAccountKeyPropName, authenticationPath):
    return BaseApi.remoteCall("GCPRestApi", "patch", requestUrl, body,
                              serviceAccountKeyPropName, authenticationPath)


@multimethod(str, dict, str, str)
def delete(requestUrl, body, serviceAccountKeyPropName, authenticationPath):
    return BaseApi.remoteCall("GCPRestApi", "delete", requestUrl, body,
                              serviceAccountKeyPropName, authenticationPath)


@multimethod(str, str, str, str)
def get(requestUrl, refreshToken, clientId, clientSecret):
    return BaseApi.remoteCall("GCPRestApi", "get", requestUrl, refreshToken, clientId,
                              clientSecret)


@multimethod(str, dict, str, str, str)
def post(requestUrl, body, refreshToken, clientId, clientSecret):
    return BaseApi.remoteCall("GCPRestApi", "post", requestUrl, body, refreshToken,
                              clientId,
                              clientSecret)


@multimethod(str, dict, dict, str, str, str)
def post(requestUrl, body, headers, refreshToken, clientId, clientSecret):
    return BaseApi.remoteCall("GCPRestApi", "post", requestUrl, body, headers,
                              refreshToken,
                              clientId, clientSecret)


@multimethod(str, dict, str, str, str)
def put(requestUrl, body, refreshToken, clientId, clientSecret):
    return BaseApi.remoteCall("GCPRestApi", "put", requestUrl, body, refreshToken,
                              clientId,
                              clientSecret)


@multimethod(str, dict, str, str, str)
def patch(requestUrl, body, refreshToken, clientId, clientSecret):
    return BaseApi.remoteCall("GCPRestApi", "patch", requestUrl, body, refreshToken,
                              clientId,
                              clientSecret)


@multimethod(str, dict, str, str, str)
def delete(requestUrl, body, refreshToken, clientId, clientSecret):
    return BaseApi.remoteCall("GCPRestApi", "delete", body, refreshToken, clientId,
                              clientSecret)


def publish(topicId, message):
    return BaseApi.remoteCall("GCPRestApi", "publish", topicId, message)


def getProjectId():
    return BaseApi.remoteCallAsString("GCPRestApi", "getProjectId")
