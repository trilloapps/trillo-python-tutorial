import ast

import requests
from cachetools import TTLCache
from multimethods import multimethod
import config
from src.collager.pojo.ResultApi import Result


@multimethod(str, dict)
def get(url, headers):
    return exchangeObjectGet(url, headers, None)


@multimethod(str)
def get(url):
    return exchangeObjectGet(url, None, None)


@multimethod(str, dict, dict)
def post(url, body, headers):
    return exchangeObjectPost(url, body, headers, None)


@multimethod(str, dict)
def post(url, body):
    return exchangeObjectPost(url, body, None, None)


@multimethod(str, dict, dict)
def postJson(url, body, headers):
    return exchangeObjectPostJson(url, body, headers, None)


def exchangeObjectGet(requestUrl, headerDict, timeout):
    res = requests.get(requestUrl, headers=headerDict, timeout=timeout)
    return res


def exchangeObjectPost(requestUrl, body, headerDict, timeout):
    res = requests.post(requestUrl, data=body, headers=headerDict, timeout=timeout)
    return res


def exchangeObjectPostJson(requestUrl, body, headerDict, timeout):
    res = requests.post(requestUrl, json=body, headers=headerDict, timeout=timeout)
    return res

