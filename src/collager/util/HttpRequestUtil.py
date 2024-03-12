import json
import ssl
from http.client import HTTPSConnection
from urllib.parse import urlparse, quote
from src.io.util.Proxy import Proxy
from src.collager.pojo.ResultApi import Result
from src.collager.util.LogApi import Log


class HttpRequestUtil:

    @staticmethod
    def get(path):
        try:
            url = urlparse(Proxy.getServerUrl() + path)
            headers = {
                "Authorization": "Bearer " + Proxy.getAccessToken(),
                "x-org-name": Proxy.getOrgName(),
                "x-app-name": Proxy.getAppName()
            }
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE

            conn = HTTPSConnection(url.netloc, context=ssl_context)
            conn.request("GET", quote(url.geturl(), safe=':/=?&'), headers=headers)
            response = conn.getresponse()

            content = response.read().decode('utf-8')

            try:
                result = json.loads(content)
                return result
            except json.JSONDecodeError:
                # Not a valid JSON response, return content as string
                return content
        except Exception as exc:
            Log.error("Failed GET call: " + str(exc))
            return Result.getFailedResult("Failed GET call: " + str(exc))

    @staticmethod
    def post(path, body):
        try:
            url = urlparse(Proxy.getServerUrl() + path)
            headers = {
                "Authorization": "Bearer " + Proxy.getAccessToken(),
                "x-org-name": Proxy.getOrgName(),
                "x-app-name": Proxy.getAppName(),
                "Content-Type": "application/json"
            }

            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            if isinstance(body, dict):
                body_str = json.dumps(body, indent=2)
            elif isinstance(body, list):
                body_str = json.dumps(body, indent=2)
            elif isinstance(body, Result):
                body_str = json.dumps(vars(body), indent=2)
            else:
                body_str = json.dumps(body, indent=2)
            conn = HTTPSConnection(url.netloc, context=ssl_context)
            conn.request("POST", quote(url.geturl(), safe=':/=?&'), body=body_str, headers=headers)
            response = conn.getresponse()

            content = response.read().decode('utf-8')

            try:
                result = json.loads(content)
                return result
            except json.JSONDecodeError:
                # Not a valid JSON response, return content as string
                return content
        except Exception as exc:
            Log.error("Failed POST call: " + str(exc))
            return Result.getFailedResult("Failed POST call: " + str(exc))

    @staticmethod
    def delete(path):
        try:
            url = urlparse(Proxy.getServerUrl() + path)
            headers = {
                "Authorization": "Bearer " + Proxy.getAccessToken(),
                "x-org-name": Proxy.getOrgName(),
                "x-app-name": Proxy.getAppName(),
                "Content-Type": "application/json"
            }
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            conn = HTTPSConnection(url.netloc, context=ssl_context)
            conn.request("DELETE", quote(url.geturl(), safe=':/=?&'), headers=headers)
            response = conn.getresponse()

            content = response.read().decode('utf-8')

            try:
                result = json.loads(content)
                return result
            except json.JSONDecodeError:
                # Not a valid JSON response, return content as string
                return content
        except Exception as exc:
            Log.error("Failed DELETE call: " + str(exc))
            return Result.getFailedResult("Failed DELETE call: " + str(exc))

    @staticmethod
    def HttpResponseToString(res):
        if isinstance(res, str):
            return res
        if res is not None:
            return json.dumps(res, indent=2)
        return None

    @staticmethod
    def HttpResponseToBoolean(res):
        if isinstance(res, bool):
            return res
        return False

    @staticmethod
    def getHttpClient():
        try:
            def trust_all_certs(arg0, arg1):
                return None

            trust_all_manager = ssl.SSLContext()
            trust_all_manager.verify_mode = ssl.CERT_NONE
            trust_all_manager.check_hostname = False
            trust_all_manager.set_default_verify_paths()
            trust_all_manager.set_ciphers('DEFAULT')
            trust_all_manager.set_alpn_protocols([])

            conn = HTTPSConnection("example.com", context=trust_all_manager)
            conn.connect()

            return conn
        except Exception as e:
            return None
