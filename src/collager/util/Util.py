from src.collager.pojo.ResultApi import Result

import json
from datetime import datetime
from typing import List, Dict, Any


class Util:
    @staticmethod
    def asJSONPrettyString(obj: Any) -> str:
        try:
            return json.dumps(obj, indent=4, sort_keys=True)
        except Exception as exc:
            raise RuntimeError("Failed to stringify object.\n" + str(exc))

    @staticmethod
    def asJSONString(obj: Any) -> str:
        try:
            return json.dumps(obj)
        except Exception as exc:
            raise RuntimeError("Failed to stringify object.\n" + str(exc))

    @staticmethod
    def fromJSONString(json_str: str, cls: Any) -> Any:
        try:
            return json.loads(json_str, cls)
        except Exception as exc:
            raise RuntimeError("Failed to make object from string.\n" + str(exc))

    @staticmethod
    def fromJSONStringAsMap(json_str: str) -> Dict[str, Any]:
        try:
            return json.loads(json_str)
        except Exception as exc:
            raise RuntimeError("Failed to make object from string.\n" + str(exc))

    @staticmethod
    def saveAsJSONString(file_path: str, obj: Any) -> None:
        try:
            with open(file_path, 'w') as file:
                json.dump(obj, file)
        except Exception as exc:
            raise RuntimeError("Failed to save object as JSON.\n" + str(exc))

    @staticmethod
    def fromStringToDate(date_str: str, format: str = "%Y-%m-%d %H:%M:%S") -> datetime:
        try:
            return datetime.strptime(date_str, format)
        except Exception as exc:
            raise ValueError("Failed to parse date string.\n" + str(exc))

    @staticmethod
    def fromDateToString(date: datetime, format: str = "%Y-%m-%d %H:%M:%S") -> str:
        try:
            return date.strftime(format)
        except Exception as exc:
            raise ValueError("Failed to format date.\n" + str(exc))

    @staticmethod
    def genRandomAlphaNum(length: int) -> str:
        # Implementation of genRandomAlphaNum method is omitted as it is not directly translatable to Python
        pass

    @staticmethod
    def mapByDisplayNames(input_map: Dict[str, Any], names: List[str], displayNames: List[str]) -> Dict[str, Any]:
        # Implementation of mapByDisplayNames method is omitted as it requires specific input and output formats
        pass

    @staticmethod
    def listByDisplayNames(input_list: List[Dict[str, Any]], names: List[str], displayNames: List[str]) -> List[
        Dict[str, Any]]:
        # Implementation of listByDisplayNames method is omitted as it requires specific input and output formats
        pass

    @staticmethod
    def deepCopy(input_map: Dict[str, Any]) -> Dict[str, Any]:
        # Implementation of deepCopy method is omitted as it requires JSON serialization/deserialization
        pass

    @staticmethod
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

    @staticmethod
    def convertToListOfDict(input_object):
        if isinstance(input_object, list):
            # Assuming each item in the list is a dictionary
            return input_object
        elif isinstance(input_object, dict):
            # If input_object is a single dictionary, convert it to a list with one element
            return [input_object]
        else:
            return []

    @staticmethod
    def convertToList(input_object):
        if isinstance(input_object, list):
            return input_object
        else:
            return []

    @staticmethod
    def convertToInt(input_object):
        if isinstance(input_object, int):
            return int(input_object)
        else:
            return -1

    @staticmethod
    def convertToDict(input_object):
        if isinstance(input_object, dict):
            return dict(input_object)
        else:
            return {}

    @staticmethod
    def convertToBool(input_object):
        if isinstance(input_object, bool):
            return bool(input_object)
        else:
            return False
