from src.collager.util.LogApi import Log


class RestOp:
    def __init__(self, opName, opManager, queueSize):
        super().__init__()
        self.setup(opName, opManager, queueSize)

    def start(self):
        Log.info("Starting: " + self.opName)
        self.startRunning()

    def doCommand(self, command):
        pass

    def completeOp(self):
        pass
