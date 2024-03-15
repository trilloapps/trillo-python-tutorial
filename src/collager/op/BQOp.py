from src.collager.util.LogPy import Log


class BQOp:
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
