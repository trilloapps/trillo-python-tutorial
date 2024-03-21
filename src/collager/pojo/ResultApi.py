import logging

class Result:
    SUCCESS = "success"
    FAILED = "failed"
    UNKNOWN = "unknown"

    _rtag = "_r_"
    LOG = logging.getLogger(__name__)

    def __init__(self):
        self._name = None
        self.status = self.UNKNOWN
        self.message = None
        self.namedMessages = None
        self.props = None
        self.data = None
        self.code = 0
        self.logs = None
        self._rtag = "_r_"

    # def __init__(self, status):
    #     self.status = status
    #
    # def __init__(self, status, message):
    #     self.status = status
    #     self.message = message

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status
        if self.message is None and status == self.FAILED:
            self.message = "Operation failed, please see the errors below"

    def getMessage(self):
        return self.message

    def setMessage(self, message):
        self.message = message

    def getNamedMessages(self):
        return self.namedMessages

    def addMessage(self, name, message):
        if self.namedMessages is None:
            self.namedMessages = []
        named_message = self.NamedMessage(name, message)
        self.namedMessages.append(named_message)

    def getDetailMessage(self):
        s = self.message if self.message is not None else ""
        if self.namedMessages is not None:
            for named_message in self.namedMessages:
                s += (s + "<br/>" if len(s) > 0 else "") + named_message.getNameAndMessage()
        return s

    def getProps(self):
        return self.props

    def setProps(self, props):
        self.props = props

    def addProp(self, name, value):
        if self.props is None:
            self.props = {}
        self.props[name] = value

    def getProp(self, name):
        return self.props[name] if self.props is not None and name in self.props else None

    def isFailed(self):
        return self.FAILED == self.status

    def isSuccess(self):
        return self.SUCCESS == self.status

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    @staticmethod
    def makeResult(status, message):
        r = Result()
        r.setStatus(status)
        r.setMessage(message)
        return r

    @staticmethod
    def makeResultWithData(status, message, data):
        r = Result()
        r.setStatus(status)
        r.setMessage(message)
        r.setData(data)
        return r

    class NamedMessage:
        def __init__(self, name, message):
            self.name = name
            self.message = message

        def getName(self):
            return self.name

        def getMessage(self):
            return self.message

        def getNameAndMessage(self):
            return f"{self.name} : {self.message}"

    def getCode(self):
        return self.code

    def setCode(self, code):
        self.code = code

    def get_rtag(self):
        return self._rtag

    def set_rtag(self, _rtag):
        # immutable, setter to keep JSON parser happy
        pass

    @staticmethod
    def getInternalError(exc):
        Result.LOG.error(str(exc))
        result = Result()
        result.setStatus(Result.FAILED)
        result.setMessage(str(exc))
        result.setCode(500)  # Internal Server Error
        return result

    @staticmethod
    def getBadRequestError():
        result = Result()
        result.setStatus(Result.FAILED)
        result.setMessage("Bad request")
        result.setCode(400)  # Bad Request
        return result

    @staticmethod
    def getNotFoundError():
        Result.LOG.debug("Not found")
        result = Result()
        result.setStatus(Result.FAILED)
        result.setMessage("Not found")
        result.setCode(404)  # Not Found
        return result

    @staticmethod
    def getNotYetImplementedError():
        result = Result()
        result.setStatus(Result.FAILED)
        result.setMessage("Not yet implemented")
        result.setCode(500)  # Internal Server Error
        return result

    @staticmethod
    def getBadRequestErrorWithMsg(msg):
        result = Result.getBadRequestError()
        result.setMessage(msg)
        return result

    @staticmethod
    def getNotFoundErrorWithMsg(msg):
        result = Result.getNotFoundError()
        result.setMessage(msg)
        return result

    @staticmethod
    def getUnauthorizedError():
        result = Result()
        result.setStatus(Result.FAILED)
        result.setMessage("Unauthorized")
        result.setCode(401)  # Unauthorized
        return result

    @staticmethod
    def getUnauthorizedErrorWithMsg(msg):
        result = Result.getUnauthorizedError()
        result.setMessage(msg)
        return result

    @staticmethod
    def getSuccessResult():
        return Result.getSuccessResultWithMsg("Success")

    @staticmethod
    def getSuccessResultWithData(data):
        return Result.getSuccessResultWithMsgAndData("Success", data)

    @staticmethod
    def getSuccessResultWithMsg(message):
        return Result.getSuccessResultWithMsgAndData(message, None)

    @staticmethod
    def getSuccessResultWithMsgAndData(message, data):
        result = Result()
        result.setStatus(Result.SUCCESS)
        result.setMessage(message)
        result.setData(data)
        result.setCode(200)  # OK
        return result

    @staticmethod
    def getFailedResult(message):
        result = Result()
        result.setStatus(Result.FAILED)
        result.setMessage(message)
        result.setCode(500)  # Internal Server Error
        return result

    @staticmethod
    def getFailedResultWithCode(message, code):
        result = Result()
        result.setStatus(Result.FAILED)
        result.setMessage(message)
        result.setCode(code)
        return result

    def getLogs(self):
        return self.logs

    def setLogs(self, logs):
        self.logs = logs

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def to_dict(self):
        result_dict = {
            "status": self.status,
            "message": self.message,
            "namedMessages": [
                {"name": named_message.name, "message": named_message.message}
                for named_message in (self.namedMessages or [])
            ],
            "props": self.props or {},
            "data": self.data,
            "code": self.code,
            "logs": self.logs or [],
            "_name": self._name,
        }
        return result_dict

    def convertResultToDict(self):
        result_dict = {
            "status": self.status,
            "message": self.message,
            "namedMessages": [
                {"name": named_message.name, "message": named_message.message}
                for named_message in (self.namedMessages or [])
            ],
            "props": self.props or {},
            "data": self.data,
            "code": self.code,
            "logs": self.logs or [],
            "_name": self._name,
        }
        return result_dict

    @classmethod
    def convertDictToResult(cls, result_dict):
        result = cls()
        result.setStatus(result_dict.get("status", Result.UNKNOWN))
        result.setMessage(result_dict.get("message"))
        result.setData(result_dict.get("data"))
        result.setCode(result_dict.get("code", 0))

        named_messages = result_dict.get("namedMessages", [])
        for named_message in named_messages:
            result.addMessage(named_message.get("name"), named_message.get("message"))

        props = result_dict.get("props", {})
        for name, value in props.items():
            result.addProp(name, value)

        result.setLogs(result_dict.get("logs", []))
        result.setName(result_dict.get("_name"))

        return result
