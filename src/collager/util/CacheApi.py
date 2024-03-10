from src.collager.util.HttpRequestUtil import HttpRequestUtil
cacheBaseEndpoint = "/api/v1.1/cache"


def get(cacheName, key):
    return HttpRequestUtil.get(cacheBaseEndpoint + "/" + cacheName + "/get?key=" + key)

def put(cacheName, key, value):
    body = {"key": key,
            "value": value}
    return HttpRequestUtil.post(cacheBaseEndpoint + "/put/" + cacheName, body)


def remove(cacheName, key):
    body = {"key": key}
    return HttpRequestUtil.post(cacheBaseEndpoint + "/remove/" + cacheName, body)


def clear(cacheName):
    body = {}
    return HttpRequestUtil.post(cacheBaseEndpoint + "/clear/" + cacheName, body)


def putNoLock(cacheName, key, value):
    body = {"key": key,
            "value": value}
    return HttpRequestUtil.post(cacheBaseEndpoint + "/putNoLock/" + cacheName, body)

def getNoLock(cacheName, key):
    return HttpRequestUtil.get(cacheBaseEndpoint + "/getNoLock/" + cacheName + "?key=" + key)

def removeNoLock(cacheName, key):
    body = {"key": key}
    return HttpRequestUtil.post(cacheBaseEndpoint + "/removeNoLock/" + cacheName, body)

def publishMessage(topic, message):
    body = {"topic": topic,
            "message": message}
    return HttpRequestUtil.post(cacheBaseEndpoint + "/publishMessage", body)
