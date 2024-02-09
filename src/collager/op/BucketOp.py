import os
import json
from typing import List, Dict, Any

from src.collager.util.LogApi import Log


class BucketOp:
    DEFAULT_QUEUE_SIZE = 1000

    def __init__(self, opName: str, params: Dict[str, Any], *keys: Any):
        self.opName = opName
        self.format = params.get("fileFormat")
        self.fileName = ""
        self.bucketFileName = ""
        self.name = ""
        self.serviceAccount = None
        self.bucketName = None
        self.bucketFolderName = None
        self.isTemp = False
        self.overwrite = False
        self.file = None
        self.fw = None
        self.os = None
        self.bw = None
        self.csvWriter = None
        self.separatorChar = None
        self.columnNames = None
        self.columnNameLine = None
        self.cancelled = False

        missingKeys = ["bucketName", "bucketFolderName", "serviceAccount", "simpleFileName", "fileFormat"]
        missingKeys = [key for key in missingKeys if key not in params]
        if missingKeys:
            raise RuntimeError("createBucketOp(), missing parameters: " + str(missingKeys))

        queueSize = params.get("queueSize", self.DEFAULT_QUEUE_SIZE)

        if keys:
            self.opManager = keys[0]

        self.setup(opName, None, params.get("bucketName"), params.get("bucketFolderName"),
                   params.get("serviceAccount"), params.get("fileFormat"),
                   params.get("simpleFileName"), params.get("isTemp"),
                   params.get("overwrite"), queueSize)

        if self.format == "csv":
            self.setupCSVParams(params.get("separatorChar"), params.get("columnNames"),
                                params.get("columnNameLine"))

    def setup(self, opName: str, opManager, bucketName: str, bucketFolderName: str,
              serviceAccount: str, format: str, simpleFileName: str,
              isTemp: bool, overwrite: bool, queueSize: int):
        self.opName = opName
        self.bucketName = bucketName
        self.bucketFolderName = bucketFolderName
        self.serviceAccount = serviceAccount
        self.format = format
        self.isTemp = isTemp
        self.overwrite = overwrite
        folderString = "/" + bucketFolderName if bucketFolderName else ""
        self.fileName = f"{bucketName}{folderString}/{simpleFileName}"
        self.bucketFileName = f"{folderString}/{simpleFileName}"

    def setupCSVParams(self, separatorChar: str, columnNames: List[str], columnNameLine: int):
        self.separatorChar = separatorChar
        self.columnNames = columnNames
        self.columnNameLine = columnNameLine

    def start(self):
        print("Starting: " + self.opName)
        if self.isTemp:
            self.file = os.path.join("/tmp", self.fileName)
        else:
            self.file = self.fileName

        self.name = os.path.basename(self.file)

        if not self.overwrite and os.path.exists(self.file):
            raise RuntimeError("File exists, overwrite is not permitted")

        dir = os.path.dirname(self.file)
        if not os.path.exists(dir):
            os.makedirs(dir)

        if self.format == "csv":
            if not self.columnNames or len(self.columnNames) == 0:
                raise RuntimeError("Invalid value for 'columnName' parameter")
            self.csvWriter = CSVWriter(self.file, self.separatorChar, self.columnNames, self.columnNameLine)
        else:
            try:
                self.fw = open(self.file, "w", encoding="utf-8")
                self.bw = self.fw
            except Exception as exc:
                if self.bw:
                    self.bw.close()
                if self.fw:
                    self.fw.close()
                raise RuntimeError("Failed to write file: " + self.name + ", Error: " + str(exc))

        self.startRunning()

    def doCommand(self, command):
        command_type = command.type
        if command_type == "write":
            self.doWrite(command)
        elif command_type == "copyToBucket":
            self.doCopyToBucket(command)
        elif command_type == "stop":
            self.doStop(command)
        elif command_type == "close":
            self.doClose()
        else:
            Log.error("Invalid command, commandType : " + str(command.type))

    def doWrite(self, command):
        if "ndjson" in self.format:
            self.doWriteNdjson(command)
        elif self.format == "csv":
            self.doWriteCSV(command)
        elif self.format == "string":
            self.doWriteString(command)
        else:
            Log.error("In write no matching format data will go missing ")

    def doClose(self):
        if self.csvWriter:
            self.csvWriter.close()
        else:
            if self.bw:
                self.bw.close()
            if self.fw:
                self.fw.close()

    def doCopyToBucket(self, command):
        pass

    def doWriteNdjson(self, command):
        pass

    def doWriteCSV(self, command):
        pass

    def doWriteString(self, command):
        pass

    def doStop(self, command):
        self.doClose()
        if command.deleteOnStop and self.file:
            os.remove(self.file)
        self.stopRunning()

    def close(self):
        pass

    def write(self, obj):
        pass

    def copyToBucket(self):
        pass

    def logFileSize(self):
        pass

    def stop(self, deleteOnStop):
        pass


class CSVWriter:

    def __init__(self, file: str, separatorChar: str, columnNames: List[str], columnNameLine: int):
        pass

    def addRows(self, rows: List[Dict[str, Any]]):
        pass

    def close(self):
        pass
