import threading
from concurrent.futures import ThreadPoolExecutor
from queue import Queue
import json


class BucketConcurrentReadOp:
    DEFAULT_CONCURRENT_TASKS = 50

    def __init__(self, opName, params):
        self.opName = opName
        self.name = ""
        self.bucketName = None
        self.bucketFolderName = None
        self.numberOfConcurrentReadTasks = self.DEFAULT_CONCURRENT_TASKS
        self.executor = None
        self.cancelled = False
        self.allFilesAdded = False
        self.format = ""
        self.filesQueue = Queue(100)

        missingKeys = [key for key in ["bucketFolderName", "serviceAccount"] if key not in params]
        if missingKeys:
            raise RuntimeError("BucketConcurrentReadOp(), missing parameters: " + str(missingKeys))

        queueSize = params.get("queueSize", 100)
        self.numberOfConcurrentReadTasks = params.get("numberOfConcurrentReadTasks", self.DEFAULT_CONCURRENT_TASKS)

        self.setup(opName, None, params.get("bucketName"), params.get("bucketFolderName"), params.get("format"),
                   queueSize, self.numberOfConcurrentReadTasks)

    def setup(self, opName, opManager, bucketName, bucketFolderName, format, queueSize, numberOfConcurrentReadTasks):
        self.opName = opName
        self.bucketName = bucketName
        self.bucketFolderName = bucketFolderName
        self.format = format
        self.numberOfConcurrentReadTasks = numberOfConcurrentReadTasks

    def start(self):
        print("Starting: " + self.opName)
        self.executor = ThreadPoolExecutor(max_workers=self.numberOfConcurrentReadTasks)
        self.do_start()

    def do_start(self):
        pageSize = 100
        pageToken = None

        while True:
            page = self.get_files_page(pageToken, pageSize)
            self.add_read_tasks(page)
            pageToken = page.get("nextPageToken")
            if pageToken is None:
                if self.executor._work_queue.empty():
                    fileContent = self.FileContent()
                    self.filesQueue.put(fileContent)
                self.allFilesAdded = True
                break

    def get_files_page(self, pageToken, pageSize):
        # Function implementation
        pass

    def add_read_tasks(self, page):
        # Function implementation
        pass

    def do_stop(self):
        pass

    def close(self):
        pass

    def stop(self, deleteOnStop):
        pass

    def completeOp(self):
        pass

    def getBucket(self):
        return self.bucketName

    def convert(self, data):
        pass

    class StartCommand:
        def __init__(self):
            self.type = "start"

    class StopCommand:
        def __init__(self, deleteOnStop):
            self.type = "stop"
            self.deleteOnStop = deleteOnStop

    class CloseCommand:
        def __init__(self):
            self.type = "close"

    class FileContent:
        def __init__(self):
            self.fileName = None
            self.content = None
            self.failed = False
            self.errorMessage = None

    class FileReadTask:
        def __init__(self, file):
            self.file = file

        def run(self):
            # Function implementation
            pass
