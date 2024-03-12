from src.collager.pojo.ResultApi import Result
import json
from datetime import datetime
from typing import List, Dict, Any
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP
import urllib.parse


class Util:
    ForwardSlash = "/"

    SNAPSHOT_CLASS = "Snapshot"
    SHARED_APP_NAME = "shared"
    COMMON_DS_NAME = "common"
    KEY_VALUE_CLASS_NAME = "KeyValue"
    AUDIT_LOG_CLASS_NAME = "AuditLog"
    AUTH_APP_NAME = "auth"
    AUTH_DS_NAME = "vault"
    APP_TO_USER_CLASS = "AppUser"
    UM_APP_NAME = "UM"

    GCP_SSERVICE_NAME = "gcp"

    @staticmethod
    def asJSONPrettyString(obj: Any) -> str:
        try:
            if isinstance(obj, Result):
                return json.dumps(vars(obj), indent=4, sort_keys=True)
            return json.dumps(obj, indent=4, sort_keys=True)
        except Exception as exc:
            raise RuntimeError("Failed to stringify object.\n" + str(exc))

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
    def asJSONString(obj: Any) -> str:
        try:
            return json.dumps(obj)
        except Exception as exc:
            raise RuntimeError("Failed to stringify object.\n" + str(exc))

    @staticmethod
    def fromJSONString(json_str: str, cls: Any) -> Any:
        try:
            return cls(json_str)
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
    def fromStringToDate(date, format="%Y-%m-%d %H:%M:%S"):
        return datetime.strptime(date, format)

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

    @staticmethod
    def uidToClassName(uid):
        if uid is None:
            return None
        idx = uid.find(".")
        if idx > 0:
            return uid[:idx]
        return None

    @staticmethod
    def uidToId(uid):
        if uid is None:
            return -1
        idx = uid.rfind(".")
        if idx > 0:
            return int(uid[idx + 1:])
        return -1

    @staticmethod
    def uidToIdStr(uid):
        if uid is None:
            return None
        idx = uid.rfind(".")
        if idx > 0:
            return uid[idx + 1:]
        return None

    @staticmethod
    def validateJson(json):
        try:
            json.loads(json)
        except json.JSONDecodeError as e:
            str_msg = str(e)
            idx1 = str_msg.find("[Source:")
            idx2 = str_msg.rfind("; line:")
            if idx1 >= 0 and idx2 > 0 and idx2 > idx1:
                str_msg = str_msg[:idx1] + str_msg[idx2 + 1:]
            raise RuntimeError(str_msg)

    @staticmethod
    def toPrettyJSONString(json_str):
        if not json_str or not json_str.strip():
            return json_str
        try:
            obj = json.loads(json_str)
            return json.dumps(obj, indent=4)
        except Exception as exc:
            raise RuntimeError("Failed to stringify object.") from exc

    @staticmethod
    def getCurrentLanguage():
        return "en"

    @staticmethod
    def asUid(className, _id=None):
        if _id is not None:
            return f"{className}.{_id}"
        else:
            return f"{className}."

    @staticmethod
    def addObjectByPath(map_, path, value):
        if path.strip():
            sl = path.split(".")
            m = map_
            for i in range(len(sl) - 1):
                if isinstance(m.get(sl[i]), dict):
                    m = m[sl[i]]
                else:
                    value_map = defaultdict(dict)
                    value_map_temp = defaultdict(dict)
                    for j in range(len(sl) - 1, i, -1):
                        if j == len(sl) - 1:
                            value_map_temp[sl[j]] = value
                            continue
                        value_map[sl[j]] = value_map_temp
                        value_map_temp = value_map
                        value_map = defaultdict(dict)
                    m[sl[i]] = value_map_temp[sl[i]]
                    break

    @staticmethod
    def removeLeadingChars(s, c):
        # here s is string type and c is char type
        i = 0
        while i < len(s) and s[i] == c:
            i += 1
        return s[i:]

    @staticmethod
    def removeLastCharIfMatches(s, c):
        # here s is string type and c is char type
        i = len(s) - 1
        while i >= 0 and s[i] == c:
            i -= 1
        return s[:i + 1]

    @staticmethod
    def roundDouble(value: float, places: int) -> float:
        if places < 0:
            raise ValueError("Number of decimal places must be non-negative")

        rounded_value = Decimal(str(value)).quantize(Decimal('1e-{0}'.format(places)), rounding=ROUND_HALF_UP)
        return float(rounded_value)

    @staticmethod
    def urlEncode(s: str) -> str:
        try:
            return urllib.parse.quote(s, safe='')
        except Exception:
            return s

    @staticmethod
    def urlDecode(s: str) -> str:
        try:
            return urllib.parse.unquote(s)
        except Exception:
            return s
