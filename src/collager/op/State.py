from src.collager.op.BucketOp import BucketOp
from src.collager.op.DbOp import DbOp
from src.collager.op.OpManager import OpManager


class State:
    def __init__(self, name=None, enclosingState=None):
        super().__init__()
        self.name = name
        self.enclosingState = enclosingState
        self.bucketOps = {}
        self.dbOps = {}
        self.bqOps = {}
        self.restOps = {}
        self.errors = []
        self.opManager = None
        self.successCount = 0
        self.failureCount = 0

    def getBucketOp(self, opName):
        return self.bucketOps.get(opName)

    def setBucketOp(self, opName, bucketOp):
        self.bucketOps[opName] = bucketOp

    def getDbOp(self, opName):
        return self.dbOps.get(opName)

    def setDbOp(self, opName, dbOp):
        self.dbOps[opName] = dbOp

    def getBqOp(self, opName):
        return self.bqOps.get(opName)

    def setBqOp(self, opName, bqOp):
        self.bqOps[opName] = bqOp

    def getRestOp(self, opName):
        return self.restOps.get(opName)

    def setRestOp(self, opName, restOp):
        self.restOps[opName] = restOp

    def getOpManager(self):
        return self.opManager

    def setOpManager(self, opManager):
        self.opManager = opManager

    def createBucketOpIfNotExists(self, opName, params):
        if opName not in self.bucketOps:
            bucketOp = BucketOp(opName, params, self.opManager if self.opManager else None)
            self.bucketOps[opName] = bucketOp
            bucketOp.start()

    def createDbOpIfNotExists(self, opName, params):
        if opName not in self.dbOps:
            dbOp = DbOp(opName, self._getOpManager(), params)
            self.dbOps[opName] = dbOp
            dbOp.start()

    def completeOps(self):
        for bucketOp in self.bucketOps.values():
            bucketOp.completeOp()

        for dbOp in self.dbOps.values():
            dbOp.completeOp()

    def select(self, *keys):
        return [{key: self.get(key) for key in keys if key not in self}]

    def addError(self, sourceName, message):
        error = [{"sourceName": sourceName, "level": "error", "message": message}]
        if self.name:
            error["name"] = self.name
        self.errors.append(error)

    def addCritical(self, sourceName, message):
        self.errors.append([{"sourceName": sourceName, "level": "critical", "message": message}])

    def getErrors(self):
        return self.errors

    def hasErrors(self):
        return len(self.errors) > 0

    def _getOpManager(self):
        if not self.opManager:
            self.opManager = OpManager()
        return self.opManager

    def getEnclosingState(self):
        return self.enclosingState
