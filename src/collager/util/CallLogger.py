import uuid


class CallLogger:
    def __init__(self):
        self.level = 2
        self.collectCallLogs = False
        self.logs = []
        self.txId = str(uuid.uuid4())

    def isDebugOn(self):
        return self.level <= 1

    def setDebugLevel(self, debugOn):
        if debugOn:
            self.setLevel(1)
        else:
            self.unsetLevel(1)

    def isInfoOn(self):
        return self.level <= 2

    def setInfoLevel(self, infoOn):
        if infoOn:
            self.setLevel(2)
        else:
            self.unsetLevel(2)

    def isWarningOn(self):
        return self.level <= 3

    def setWarningLevel(self, warningOn):
        if warningOn:
            self.setLevel(3)
        else:
            self.unsetLevel(3)

    def isErrorOn(self):
        return self.level <= 4

    def setErrorLevel(self, errorOn):
        if errorOn:
            self.setLevel(4)
        else:
            self.unsetLevel(4)

    def debug(self, msg):
        if not self.collectCallLogs or self.level > 1:
            return
        self.addMsg("Debug", msg)

    def info(self, msg):
        if not self.collectCallLogs or self.level > 2:
            return
        self.addMsg("Info", msg)

    def warn(self, msg):
        if not self.collectCallLogs or self.level > 3:
            return
        self.addMsg("Warn", msg)

    def error(self, msg):
        if not self.collectCallLogs or self.level > 4:
            return
        self.addMsg("Error", msg)

    def getLogs(self):
        return self.logs

    def setLevel(self, n):
        if self.level > n:
            self.level = n

    def unsetLevel(self, n):
        if self.level <= n:
            self.level = n + 1

    def addMsg(self, type, msg):
        self.logs.append(f"{type} : {msg}")

    def setLogLevel(self, logLevel):
        if logLevel == "debug":
            self.setDebugLevel(True)
        elif logLevel == "info":
            self.setInfoLevel(True)
        elif logLevel == "warn":
            self.setWarningLevel(True)
        elif logLevel == "error":
            self.setErrorLevel(True)

    def isCollectCallLogs(self):
        return self.collectCallLogs

    def setCollectCallLogs(self, collectCallLogs):
        self.collectCallLogs = collectCallLogs
