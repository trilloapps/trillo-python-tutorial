import json
import logging
import os
import uuid
from datetime import time
from typing import Union



from src.collager.pojo.ResultApi import Result
from src.collager.util.Util import Util
from src.io.util.Proxy import Proxy


class BaseApi:
    log = logging.getLogger(__name__)

    @staticmethod
    def asJSONPrettyString(my_dict):
        json_string = json.dumps(my_dict, indent=2, sort_keys=True)
        return json_string

    @staticmethod
    def asJSONString(obj: object) -> str:
        return Util.asJSONString(obj)


    @staticmethod
    def successResult() -> Result:
        return Result.getSuccessResult()

    @staticmethod
    def successResult(msg: str) -> Result:
        return Result.getSuccessResult(msg)

    @staticmethod
    def successResult(msg: str, data: object) -> Result:
        return Result.getSuccessResult(msg, data)

    @staticmethod
    def errorResult(msg: str) -> Result:
        return Result.getFailedResult(msg)

    @staticmethod
    def errorResult(msg: str, code: int) -> Result:
        return Result.getFailedResult(msg, code)

    @staticmethod
    def extractMessage(obj: object) -> str:
        return obj.getDetailMessage() if isinstance(obj, Result) else "Unknown"

    @staticmethod
    def isResult(obj: object) -> bool:
        return isinstance(obj, Result)

    @staticmethod
    def isResultOrNull(obj: object) -> bool:
        return obj is None or isinstance(obj, Result)

    @staticmethod
    def UUID() -> str:
        return str(uuid.uuid4())

    @staticmethod
    def uidToClassName(uid: str) -> str:
        return Util.uidToClassName(uid)

    @staticmethod
    def uidToId(uid: str) -> int:
        return Util.uidToId(uid)

    @staticmethod
    def uidToIdStr(uid: str) -> str:
        return Util.uidToIdStr(uid)

    @staticmethod
    def waitForMillis(tm: int) -> Result:
        try:
            time.sleep(tm / 1000)
            return Result.getSuccessResult()
        except Exception as e:
            return Result.getFailedResult(e.getLocalizedMessage())

    @staticmethod
    def getDataServiceUrl() -> str:
        return BaseApi.remoteCallAsString("BaseApi", "getDataServiceUrl")

    @staticmethod
    def getAccessToken() -> str:
        return BaseApi.remoteCallAsString("BaseApi", "getAccessToken")

    @staticmethod
    def getStatusInformUrl() -> str:
        return BaseApi.remoteCallAsString("BaseApi", "getStatusInformUrl")

    @staticmethod
    def remoteCall(java_class_name: str, java_method_name: str, *args: object) -> object:
        return Proxy.remoteCall(java_class_name, java_method_name, args)

    @staticmethod
    def remoteCallAsResult(java_class_name: str, java_method_name: str, *args: object) -> Result:
        res = Proxy.remoteCall(java_class_name, java_method_name, args)
        if isinstance(res, Result):
            return res
        raise RuntimeError("Unexpected type")

    @staticmethod
    def remoteCallAsMap(java_class_name: str, java_method_name: str, *args: object) -> dict[
        str, Union[str, int, float, bool, None]]:
        res = Proxy.remoteCall(java_class_name, java_method_name, args)
        if isinstance(res, dict):
            return res
        if isinstance(res, Result):
            result = res
            raise RuntimeError(result.getMessage())
        raise RuntimeError("Unexpected type")

    @staticmethod
    def remoteCallAsString(java_class_name: str, java_method_name: str, *args: object) -> str:
        res = Proxy.remoteCall(java_class_name, java_method_name, args)
        if isinstance(res, str):
            return res
        if res is not None:
            return Util.asJSONPrettyString(res)
        return None

    @staticmethod
    def remoteCallAsBoolean(java_class_name: str, java_method_name: str, *args: object) -> bool:
        res = Proxy.remoteCall(java_class_name, java_method_name, args)
        if isinstance(res, bool):
            return res
        if isinstance(res, Result):
            result = res
            raise RuntimeError(result.getMessage())
        raise RuntimeError("Unexpected type")

    @staticmethod
    def remoteCallAsList(java_class_name: str, java_method_name: str, *args: object) -> list[object]:
        res = Proxy.remoteCall(java_class_name, java_method_name, args)
        if isinstance(res, list):
            return res
        if isinstance(res, Result):
            result = res
            raise RuntimeError(result.getMessage())
        raise RuntimeError("Unexpected type")

    @staticmethod
    def remoteCallAsListOfMaps(java_class_name: str, java_method_name: str, *args: object) -> list[
        dict[str, Union[str, int, float, bool, None]]]:
        res = Proxy.remoteCall(java_class_name, java_method_name, args)
        if isinstance(res, list):
            return res
        if isinstance(res, Result):
            result = res
            raise RuntimeError(result.getMessage())
        raise RuntimeError("Unexpected type")

    @staticmethod
    def app(class_name: str) -> str:
        if BaseApi.isBlank(class_name):
            return Util.SHARED_APP_NAME

        sl = class_name.split("\\.")
        if len(sl) > 2:
            # <appName>.<dsName>.<className> pattern
            # <appName>.<className> pattern
            return sl[0]

        return Util.SHARED_APP_NAME

    @staticmethod
    def app_for_function(function_name: str) -> str:
        if BaseApi.isBlank(function_name):
            return Util.SHARED_APP_NAME

        sl = function_name.split("\\.")
        if len(sl) > 2:
            # <appName>.<functionName> pattern
            return sl[0]

        return Util.SHARED_APP_NAME

    @staticmethod
    def ds(class_name: str) -> str:
        if BaseApi.isBlank(class_name):
            return Util.COMMON_DS_NAME

        sl = class_name.split("\\.")
        if len(sl) > 2:
            # <appName>.<dsName>.<className> pattern
            return sl[1]
        elif len(sl) > 1:
            # <dsName>.<className> pattern
            return sl[0]

        return Util.COMMON_DS_NAME

    @staticmethod
    def cls(class_name: str) -> str:
        if class_name is None:
            return ""

        sl = class_name.split("\\.")
        if len(sl) > 2:
            if len(sl) == 3:
                # <appName>.<dsName>.<className> pattern
                return sl[2]
            else:
                # <appName>.<dsName>.<schema>.<className> pattern
                return sl[2] + "." + sl[3]

        elif len(sl) > 1:
            # <dsName>.<className> pattern
            return sl[1]

        return class_name

    @staticmethod
    def app_from_ds(ds: str) -> str:
        if BaseApi.isBlank(ds):
            return Util.SHARED_APP_NAME

        sl = ds.split("\\.")
        if len(sl) == 2:
            # <appName>.<dsName> pattern
            return sl[0]

        return Util.SHARED_APP_NAME

    @staticmethod
    def ds_from_ds(ds_name: str) -> str:
        if BaseApi.isBlank(ds_name):
            return Util.COMMON_DS_NAME

        sl = ds_name.split("\\.")
        if len(sl) == 2:
            # <appName>.<dsName> pattern
            return sl[1]

        return ds_name

    @staticmethod
    def app_for_flow(flow_name: str) -> str:
        if BaseApi.isBlank(flow_name):
            return Util.SHARED_APP_NAME

        sl = flow_name.split("\\.")
        if len(sl) > 2:
            # <appName>.<flowName> pattern
            return sl[0]

        return Util.SHARED_APP_NAME

    @staticmethod
    def function(function_name: str) -> str:
        if BaseApi.isBlank(function_name):
            return ""

        sl = function_name.split("\\.")
        if len(sl) == 2:
            return sl[1]

        return function_name

    @staticmethod
    def schema(class_name: str) -> str:
        if class_name is None:
            return ""

        sl = class_name.split("\\.")
        if len(sl) > 1:
            return sl[len(sl) - 2]

        return ""

    @staticmethod
    def flow(flow_name: str) -> str:
        if BaseApi.isBlank(flow_name):
            return ""

        sl = flow_name.split("\\.")
        if len(sl) == 2:
            return sl[1]

        return flow_name

    @staticmethod
    def cls_without_schema(class_name: str) -> str:
        if class_name is None:
            return ""

        sl = class_name.split("\\.")
        return sl[len(sl) - 1]

    @staticmethod
    def isBlank(text):
        return not text

