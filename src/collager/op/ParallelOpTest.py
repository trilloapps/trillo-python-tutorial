from datetime import time

from src.collager.op.ParallelOp import ParallelOp
from src.collager.pojo.ResultApi import Result
from src.collager.util.Util import Util
from src.collager.util.LogApi import Log


class ParallelOpTest:
    def __init__(self):
        self.parallelOp = ParallelOp()

    def executeTest(self):
        params1 = {"value": "parameter_of_w1"}
        self.parallelOp.addWorker(Worker1(), params1)

        params2 = {"value": "parameter_of_w2"}
        self.parallelOp.addWorker(Worker2(), params2)

        self.parallelOp.execute()

        if self.parallelOp.getFailedCount() > 0:
            Log.info("Failed count: " + str(self.parallelOp.getFailedCount()))
            Log.info("Failed results message: \n" + self.parallelOp.getFailedMessages())

        results = self.parallelOp.getResults()
        Log.info("Result detail:\n" + Util.asJSONPrettyString(results))


class Worker1:
    def __init__(self):
        self.name = "Worker1"
        self.waitTime = 4

    def perform(self, params):
        Log.info(self.name + " - started")
        Log.info("Parameters: " + Util.asJSONPrettyString(params))
        time.sleep(self.waitTime)  # Assuming sleep in seconds
        Log.info(self.name + " - completed")
        return Result.getSuccessResult()


class Worker2:
    def __init__(self):
        self.name = "Worker2"
        self.waitTime = 5

    def perform(self, params):
        Log.info(self.name + " - started")
        Log.info("Parameters: " + Util.asJSONPrettyString(params))
        time.sleep(self.waitTime)  # Assuming sleep in seconds
        Log.info(self.name + " - failed")
        return Result.getFailedResult("Failed after " + str(self.waitTime) + " s")


if __name__ == "__main__":
    ParallelOpTest().executeTest()
