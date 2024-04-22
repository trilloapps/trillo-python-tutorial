import os
import io
from typing import Any, List, Optional, Tuple
from queue import Queue
from threading import Thread

from src.collager.util import StorageApi, LogApi
from src.collager.util.Util import Util


class FileWriterThread:

    def __init__(self, format: str, fileName: str, bucketFileName: str, isTemp: bool, overwrite: bool):
        self.format = format  # STRING, JSON, NDJSON, XML, CSV etc
        self.fileName = fileName
        self.bucketFileName = bucketFileName
        self.name = ""
        self.isTemp = isTemp  # if isTemp true then a file with the given name is created inside /tmp directory.
        self.overwrite = overwrite  # if false then it will throw an exception if the file already exists.
        self.file = None  # type: Optional[io.TextIOWrapper]
        self.queue = Queue(maxsize=100)
        self.myThread = None  # type: Optional[Thread]
        self.count = 0
        self.cancelled = False

    def getFileName(self) -> str:
        return self.fileName

    def getBucketFileName(self) -> str:
        return self.bucketFileName

    def isCancelled(self) -> bool:
        return self.cancelled

    def setCancelled(self, cancelled: bool) -> None:
        self.cancelled = cancelled

    def run(self) -> None:
        try:
            while True:
                c = self.queue.get()
                self.doCommand(c)
                if c.type == "stop":
                    break
        except KeyboardInterrupt:
            pass

    def start(self) -> None:
        LogApi.auditLogInfo("Starting: " + self.fileName)
        if self.isTemp:
            self.file = open(os.path.join("/tmp", self.fileName), "w", encoding="utf-8")
        else:
            self.file = open(self.fileName, "w", encoding="utf-8")

        self.name = os.path.basename(self.file.name)

        if not self.overwrite and os.path.exists(self.file.name):
            raise RuntimeError("File exists, overwrite is not permitted")

        dir_name = os.path.dirname(self.file.name)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        self.myThread = Thread(target=self.run)
        self.myThread.start()

    def doCommand(self, command: 'FileWriterThread.Command') -> None:
        if command.type == "write":
            self.doWrite(command)
        elif command.type == "copyToBucket":
            self.doCopyToBucket(command)
        elif command.type == "stop":
            self.doStop(command)
        elif command.type == "close":
            self.doClose()
        else:
            LogApi.auditLogError("Invalid command: " + command.type)

    def doWrite(self, command: 'FileWriterThread.WriteCommand') -> None:
        if self.format == "ndjson":
            self.doWriteNdjson(command)
        elif self.format == "string":
            self.doWriteString(command)

    def doClose(self):
        try:
            if self.bw:
                try:
                    self.bw.flush()
                except Exception as exc:
                    pass
                self.bw.close()
                self.bw = None
        except Exception as exc:
            pass

        try:
            if self.os:
                self.os.close()
                self.os = None
        except Exception as exc:
            pass

        try:
            if self.fw:
                self.fw.close()
                self.fw = None
        except Exception as exc:
            pass

    def doCopyToBucket(self, command: 'FileWriterThread.CopyToBucketCommand') -> None:
        LogApi.auditLogInfo("Copying to bucket: " + self.fileName)
        if command.bucketName:
            result = StorageApi.copyLargeFileToBucket(command.bucketName, command.serviceAccount, self.file.name,
                                                      self.bucketFileName)
        else:
            result = StorageApi.copyLargeFileToBucket(self.file.name, self.bucketFileName)

        if result.isFailed():
            LogApi.auditLogError(
                "Failed copy file to bucket, source file: " + self.fileName + ", target file: " + self.bucketFileName + ", bucket: " + (
                    command.bucketName if command.bucketName else "Trillo bucket") + ", error: " + result.getMessage())
        else:
            LogApi.auditLogInfo(
                "Successfully copied file to bucket, source file: " + self.fileName + ", target file: " + self.bucketFileName + ", bucket: " + (
                    command.bucketName if command.bucketName else "Trillo bucket"))

    def doWriteNdjson(self, command: 'FileWriterThread.WriteCommand') -> None:
        if isinstance(command.object, List):
            l = command.object
        else:
            l = [command.object]
        for obj in l:
            try:
                self.file.write(Util.asJSONString(obj) + "\n")
            except Exception as e:
                print(e)

    def doWriteString(self, command: 'FileWriterThread.WriteCommand') -> None:
        str_obj = str(command.object)
        try:
            self.file.write(str_obj + "\n")
        except Exception as e:
            print(e)

    def doStop(self, command: 'FileWriterThread.StopCommand') -> None:
        self.doClose()
        if command.deleteOnStop and self.file:
            os.remove(self.file.name)

    def close(self) -> None:
        c = self.CloseCommand()
        self.queue.put(c)

    def write(self, obj: Any) -> None:
        c = self.WriteCommand(obj)
        self.queue.put(c)

    def copyToBucket(self, bucketName: Optional[str] = None, serviceAccount: Optional[str] = None) -> None:
        c = self.CopyToBucketCommand(bucketName, serviceAccount)
        self.queue.put(c)

    def logFileSize(self) -> None:
        if self.file:
            LogApi.auditInfo2("BucketOp", "BucketOp file size", "fileName", self.fileName, "fileSize",
                            os.path.getsize(self.file.name))

    def stop(self, deleteOnStop: bool) -> None:
        c = self.StopCommand(deleteOnStop)
        self.queue.put(c)

    class Command:
        def __init__(self, type: str) -> None:
            self.type = type

    class WriteCommand(Command):
        def __init__(self, obj: Any) -> None:
            super().__init__("write")
            self.object = obj

    class CopyToBucketCommand(Command):
        def __init__(self, bucketName: Optional[str], serviceAccount: Optional[str]) -> None:
            super().__init__("copyToBucket")
            self.bucketName = bucketName
            self.serviceAccount = serviceAccount

    class StopCommand(Command):
        def __init__(self, deleteOnStop: bool) -> None:
            super().__init__("stop")
            self.deleteOnStop = deleteOnStop

    class CloseCommand(Command):
        def __init__(self) -> None:
            super().__init__("close")

    def queue(self, c: Command) -> None:
        self.count += 1
        self.queue.put(c)
