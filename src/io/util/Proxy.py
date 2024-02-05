import json
import requests
import logging
from typing import Dict
from src.collager.pojo.ResultApi import Result


class Proxy:
    log = logging.getLogger(__name__)
    loginResponse = None
    user = None
    serverUrl = None
    userId = None
    password = None
    orgName = "cloud"
    appName = "shared"
    tenantName = None
    accessToken = None
    privilegedMode = False
    privilegedUserMode = False

    @classmethod
    def setArgs(cls, args: Dict[str, str]):
        cls.setServerUrl(str(args.get("serverUrl", "")))
        cls.setUserId(str(args.get("userId", "")))
        cls.setPassword(str(args.get("password", "")))
        if "orgName" in args:
            cls.setOrgName(str(args["orgName"]))
        if "appName" in args:
            cls.setAppName(str(args["appName"]))
        if "tenantName" in args:
            cls.tenantName = str(args["tenantName"])

    @classmethod
    def getLoginResponse(cls) -> Dict[str, str]:
        return cls.loginResponse

    @classmethod
    def getUserId(cls) -> str:
        return cls.userId

    @classmethod
    def getOrgName(cls) -> str:
        return cls.orgName

    @classmethod
    def getAppName(cls) -> str:
        return cls.appName

    @classmethod
    def getServerUrl(cls) -> str:
        return cls.serverUrl

    @classmethod
    def setServerUrl(cls, serverUrl: str):
        cls.serverUrl = serverUrl

    @classmethod
    def setUserId(cls, userId: str):
        cls.userId = userId

    @classmethod
    def setPassword(cls, password: str):
        cls.password = password

    @classmethod
    def setOrgName(cls, orgName: str):
        cls.orgName = orgName

    @classmethod
    def setAppName(cls, appName: str):
        cls.appName = appName

    @classmethod
    def getAccessToken(cls) -> str:
        if cls.accessToken:
            return cls.accessToken
        cls.login()
        return cls.accessToken

    @classmethod
    def setAccessToken(cls, accessToken: str):
        cls.accessToken = accessToken

    @classmethod
    def isLoggedIn(cls) -> bool:
        return bool(cls.accessToken)

    @classmethod
    def login(cls) -> bool:
        data = {
            "username": cls.userId,
            "password": cls.password,
        }
        if cls.tenantName:
            data["tenant_display_name"] = cls.tenantName
        headers = {
            "Content-Type": "application/json",
            "x-org-name": "cloud"
        }
        try:
            response = requests.post(
                f"{cls.serverUrl}/ajaxLogin",
                headers=headers,
                json=data,
            )
            response.raise_for_status()
            cls.loginResponse = response.json()
            if "accessToken" not in cls.loginResponse:
                cls.log.error("Failed to login, see the response below")
                cls.log.error(response.text)
                raise RuntimeError("Failed to login, check the arguments you supplied")
            cls.user = cls.loginResponse["user"]
            cls.accessToken = cls.loginResponse["accessToken"]
            cls.log.info(f"Successfully logged in: {cls.user.get('userId')}")
            return True
        except Exception as exc:
            cls.log.error(f"Failed to login: {exc}")
            return False

    @classmethod
    def remoteCall(cls, javaClassName: str, javaMethodName: str, *args) -> object:
        data = {
            "javaClassName": javaClassName,
            "javaMethodName": javaMethodName,
            "args": args,
        }
        if cls.privilegedMode:
            data["privilegedMode"] = cls.privilegedMode
        if cls.privilegedUserMode:
            data["privilegedUserMode"] = cls.privilegedUserMode
        headers = {
            "Authorization": f"Bearer {cls.getAccessToken()}",
            "x-org-name": cls.orgName,
            "x-app-name": cls.appName,
            "Content-Type": "application/json",
        }
        try:
            response = requests.post(
                f"{cls.getServerUrl()}/ds/remoteCall",
                headers=headers,
                json=data,
            )
            response.raise_for_status()
            try:
                result = response.json()
                if isinstance(result, dict) and result.get("_rtag") == "_r_":
                    return Result.convertDictToResult(result)
                return result
            except json.JSONDecodeError:
                # Not a valid JSON response, return content as string
                return response.text
        except Exception as exc:
            cls.log.error(f"Failed remoteCall: {exc}")
            return Result.getFailedResult(f"Failed remoteCall: {exc}")

    @classmethod
    def getHttpClient(cls) -> requests.Session:
        try:
            session = requests.Session()
            session.verify = False  # Disabling SSL verification
            return session
        except Exception as e:
            cls.log.error(e)
            return None

    @classmethod
    def getIdOfCurrentUser(cls) -> str:
        return str(cls.user.get("id"))

    @classmethod
    def getIdOfCurrentUserAsLong(cls) -> int:
        return int(cls.user.get("id"))

    @classmethod
    def switchToPrivilegedMode(cls):
        cls.privilegedMode = True

    @classmethod
    def resetPrivilegedMode(cls):
        cls.privilegedMode = False

    @classmethod
    def isPrivilegedMode(cls) -> bool:
        return cls.privilegedMode

    @classmethod
    def switchToPrivilegedUserMode(cls):
        cls.privilegedUserMode = True

    @classmethod
    def resetPrivilegedUserMode(cls):
        cls.privilegedUserMode = False

    @classmethod
    def isPrivilegedUserMode(cls) -> bool:
        return cls.privilegedUserMode
