import json

from src.collager.pojo.ResultApi import Result


def convertToResult(r):
    if isinstance(r, Result):
        return r

    try:
        if isinstance(r, dict) and "_rtag" in r:
            result = Result.convertDictToResult(r)
            return result
    except Exception as exc:
        return None

    return None


def convertToListOfDict(input_object):
    if isinstance(input_object, list):
        # Assuming each item in the list is a dictionary
        return input_object
    elif isinstance(input_object, dict):
        # If input_object is a single dictionary, convert it to a list with one element
        return [input_object]
    else:
        return []


def convertToList(input_object):
    if isinstance(input_object, list):
        return input_object
    else:
        return []


def convertToInt(input_object):
    if isinstance(input_object, int):
        return int(input_object)
    else:
        return -1


def convertToDict(input_object):
    if isinstance(input_object, dict):
        return dict(input_object)
    else:
        return {}


def convertToBool(input_object):
    if isinstance(input_object, bool):
        return bool(input_object)
    else:
        return False
