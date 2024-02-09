from concurrent.futures import ThreadPoolExecutor

from src.collager.util import Util
from src.collager.util.LogApi import Log


class ParallelOp:
    executorService = ThreadPoolExecutor(max_workers=5)

    def __init__(self):
        self.callables = []
        self.futures = None
        self.results = []
        self.failedCount = 0
        self.failedMessages = ""

    def addWorker(self, worker, params):
        self.callables.append(self.WorkerThread(worker, Util.deepCopy(params)))

    def execute(self):
        try:
            self.futures = ParallelOp.executorService.invoke_all(self.callables)
            ParallelOp.executorService.shutdown()
            self.collectResult(self.futures)
        except Exception as e:
            Log.error("Failed to 'execute' a parallel op, with error: " + e.getMessage())

    def collectResult(self, futures):
        for future in futures:
            try:
                r = future.result()
                self.results.append(r)
                if r.isFailed():
                    self.failedCount += 1
                    self.failedMessages += (self.failedMessages + "\n" if len(self.failedMessages) > 0 else "") + r.getMessage()
            except Exception as e:
                Log.error("Failed to 'collectResult' of a parallel op, with error: " + e.getMessage())

    def getFailedCount(self):
        return self.failedCount

    def getFailedMessages(self):
        return self.failedMessages

    def getResults(self):
        return self.results

    class WorkerThread:
        def __init__(self, worker, params):
            self.worker = worker
            self.params = params

        def call(self):
            try:
                return self.worker.perform(self.params)
            except Exception as e:
                raise e
