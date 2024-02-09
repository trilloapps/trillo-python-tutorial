from queue import Queue
from threading import Thread
from abc import ABC, abstractmethod

from src.collager.util.LogApi import Log


class Op:
    DEFAULT_QUEUE_SIZE = 100

    def __init__(self):
        self.queue = Queue(self.DEFAULT_QUEUE_SIZE)
        self.myThread = None
        self.opName = None
        self.opManager = None

    def setup(self, opName, opManager, queueSize):
        self.opName = opName
        self.opManager = opManager

    def run(self):
        while True:
            try:
                c = self.queue.get()
                self.doCommand(c)
                if c.type == "stop":
                    break
            except Exception as exc:
                Log.error(f"{self.opName} operation run loop exception: {exc}")
                Log.error(f"{self.opName} operation run loop exception: {exc}", exc)

    def startRunning(self):
        self.myThread = Thread(target=self.run)
        self.myThread.start()
        self.opManager.register(self)

    def stopRunning(self):
        self.opManager.unregister(self)

    def getThread(self):
        return self.myThread

    def queue(self, c):
        try:
            self.queue.put(c)
        except Exception as e:
            Log.error(f"SaveDSOp - failed to put an command in the queue, command: {c.type}")

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def doCommand(self, command):
        pass

    @abstractmethod
    def completeOp(self):
        pass
