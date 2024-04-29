import os
import json
import logging
import sys
from importlib import import_module

from src.collager.pojo.ResultApi import Result
from src.io.util.Proxy import Proxy
from src.collager.util.Util import *
from src.collager.util.BaseApi import BaseApi
from src.collager.util.LogPy import Log


class RunFunction:
    log = logging.getLogger(__name__)
    defaultConfigFile = "/config/server.json"

    @staticmethod
    def main(args):
        file = RunFunction.getConfigFile(args)
        if not os.path.exists(file):
            Log.error("Missing config file, " + file)
            exit(-1)

        config = RunFunction.loadFile(file)
        if config is None:
            exit(-1)

        if not RunFunction.verifyAndUpdateConfig(config, file):
            exit(-1)

        functionDetailsFile = config.get("functionDetailsFile")
        functionDetailsFile = os.path.join(os.path.dirname(file), functionDetailsFile)
        if not os.path.exists(functionDetailsFile):
            Log.error("Missing functionDetailsFile, " + functionDetailsFile)
            exit(-1)

        functionDetails = RunFunction.loadFile(functionDetailsFile)
        if functionDetails is None or not RunFunction.verifyFunctionDetails(functionDetails, functionDetailsFile):
            exit(-1)

        functionName = functionDetails.get("functionName")
        methodName = functionDetails.get("methodName")
        Log.info("Function name: " + functionName + ", method name: " + methodName)

        parameters = functionDetails.get("parameters", {})
        Proxy.setArgs(config)

        if not Proxy.login():
            return

        RunFunction.executeFunction(functionName, methodName, parameters)
        Log.info("Done")

    @staticmethod
    def getConfigFile(args):
        currentFileDir = os.path.dirname(os.path.abspath(__file__))
        rootDir = os.path.abspath(os.path.join(currentFileDir, '..', '..'))
        return os.path.abspath(rootDir + RunFunction.defaultConfigFile)

    @staticmethod
    def loadFile(file):
        try:
            with open(file, 'r') as f:
                return json.load(f)
        except Exception as exc:
            exc.printStackTrace(exc)
            Log.error("Failed to load file, " + file)
            return None

    @staticmethod
    def verifyAndUpdateConfig(config, configFilePath):
        verified = True

        if "serverUrl" not in config:
            Log.error("Missing 'serverUrl' in " + configFilePath)
            verified = False

        if config["serverUrl"] == "<your workbench url>":
            Log.error("Trillo Workbench serverUrl is not specified. Specify it using variable serverUrl in configFile : " + configFilePath)
            verified = False

        if "functionDetailsFile" not in config:
            Log.error("Missing 'functionDetailsFile' in " + configFilePath)
            verified = False

        config.pop("userId", None)
        config.pop("password", None)

        userId = os.environ.get("TRILLO_WB_USER_ID")
        password = os.environ.get("TRILLO_WB_USER_PASSWORD")

        if userId is None:
            Log.error(
                "Trillo Workbench userId is not specified. Specify it using environment variable TRILLO_WB_USER_ID")
            verified = False

        if password is None:
            Log.error(
                "Trillo Workbench password is not specified. Specify it using environment variable TRILLO_WB_USER_PASSWORD")
            verified = False

        if verified:
            config["userId"] = userId
            config["password"] = password

        return verified

    @staticmethod
    def verifyFunctionDetails(functionDetails, functionDetailsFile):
        verified = True

        if "functionName" not in functionDetails:
            Log.error("Missing 'functionName' in " + functionDetailsFile)
            verified = False

        if "methodName" not in functionDetails:
            Log.error("Missing 'methodName' in " + functionDetailsFile)
            verified = False

        if "parameters" not in functionDetails:
            Log.error("Missing 'parameters' in " + functionDetailsFile)
            verified = False

        if not isinstance(functionDetails["parameters"], dict):
            Log.error("'parameters' is not a valid JSON object in " + functionDetailsFile)
            verified = False

        return verified

    @staticmethod
    def executeFunction(functionName, methodName, parameters):
        try:
            module = import_module("src." + functionName)
            f = getattr(module, methodName)
            res = f(parameters)
            if isinstance(res, str):
                Log.info("Result: \n" + res)
            elif isinstance(res, Result):
                Log.info("Result: \n" + BaseApi.asJSONPrettyString(Result.convertResultToDict(res)))
            else:
                Log.info("Result: \n" + BaseApi.asJSONPrettyString(res))
        except Exception as e:
            Log.error("Failed to call function: " + functionName + str(e))


if __name__ == "__main__":
    RunFunction.main(sys.argv[1:])
