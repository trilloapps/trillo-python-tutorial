from src.collager.util.BaseApi import BaseApi


class GCPRestApi:

    @staticmethod
    def get(requestUrl):
        return BaseApi.remoteCall("GCPRestApi", "get", requestUrl)

    @staticmethod
    def post(requestUrl, body):
        return BaseApi.remoteCall("GCPRestApi", "post", requestUrl, body)

    @staticmethod
    def post(requestUrl, body, headers):
        return BaseApi.remoteCall("GCPRestApi", "post", requestUrl, body, headers)

    @staticmethod
    def put(requestUrl, body):
        return BaseApi.remoteCall("GCPRestApi", "put", requestUrl, body)

    @staticmethod
    def patch(requestUrl, body):
        return BaseApi.remoteCall("GCPRestApi", "patch", requestUrl, body)

    @staticmethod
    def delete(requestUrl, body):
        return BaseApi.remoteCall("GCPRestApi", "delete", requestUrl, body)

    @staticmethod
    def get(requestUrl, serviceAccountKeyPropName, authenticationPath):
        return BaseApi.remoteCall("GCPRestApi", "get", requestUrl,
                                  serviceAccountKeyPropName,
                                  authenticationPath)

    @staticmethod
    def post(requestUrl, body, serviceAccountKeyPropName, authenticationPath):
        return BaseApi.remoteCall("GCPRestApi", "post", requestUrl, body,
                                  serviceAccountKeyPropName, authenticationPath)

    @staticmethod
    def post(requestUrl, body, headers, serviceAccountKeyPropName, authenticationPath):
        return BaseApi.remoteCall("GCPRestApi", "post", requestUrl, body, headers,
                                  serviceAccountKeyPropName, authenticationPath)

    @staticmethod
    def put(requestUrl, body, serviceAccountKeyPropName, authenticationPath):
        return BaseApi.remoteCall("GCPRestApi", "put", requestUrl, body,
                                  serviceAccountKeyPropName, authenticationPath)

    @staticmethod
    def patch(requestUrl, body, serviceAccountKeyPropName, authenticationPath):
        return BaseApi.remoteCall("GCPRestApi", "patch", requestUrl, body,
                                  serviceAccountKeyPropName, authenticationPath)

    @staticmethod
    def delete(requestUrl, body, serviceAccountKeyPropName, authenticationPath):
        return BaseApi.remoteCall("GCPRestApi", "delete", requestUrl, body,
                                  serviceAccountKeyPropName, authenticationPath)

    @staticmethod
    def get(requestUrl, refreshToken, clientId, clientSecret):
        return BaseApi.remoteCall("GCPRestApi", "get", requestUrl, refreshToken, clientId,
                                  clientSecret)

    @staticmethod
    def post(requestUrl, body, refreshToken, clientId, clientSecret):
        return BaseApi.remoteCall("GCPRestApi", "post", requestUrl, body, refreshToken,
                                  clientId,
                                  clientSecret)

    @staticmethod
    def post(requestUrl, body, headers, refreshToken, clientId, clientSecret):
        return BaseApi.remoteCall("GCPRestApi", "post", requestUrl, body, headers,
                                  refreshToken,
                                  clientId, clientSecret)

    @staticmethod
    def put(requestUrl, body, refreshToken, clientId, clientSecret):
        return BaseApi.remoteCall("GCPRestApi", "put", requestUrl, body, refreshToken,
                                  clientId,
                                  clientSecret)

    @staticmethod
    def patch(requestUrl, body, refreshToken, clientId, clientSecret):
        return BaseApi.remoteCall("GCPRestApi", "patch", requestUrl, body, refreshToken,
                                  clientId,
                                  clientSecret)

    @staticmethod
    def delete(requestUrl, body, refreshToken, clientId, clientSecret):
        return BaseApi.remoteCall("GCPRestApi", "delete", body, refreshToken, clientId,
                                  clientSecret)

    @staticmethod
    def publish(topicId, message):
        return BaseApi.remoteCall("GCPRestApi", "publish", topicId, message)

    @staticmethod
    def getProjectId():
        return BaseApi.remoteCallAsString("GCPRestApi", "getProjectId")
