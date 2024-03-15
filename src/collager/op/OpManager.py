from typing import List

from src.collager.op.BucketOp import BucketOp
from src.collager.util.CSVConst import CSVConst
from src.collager.util.LogPy import Log


class OpManager:
    def __init__(self):
        self.ops = []

    def register(self, op):
        self.ops.append(op)

    def unregister(self, op):
        self.ops.remove(op)

    def minWaitForAllOpsToEnd(self, minutes):
        self.waitForAllOpsToEnd(minutes * 60 * 1000)

    def waitForAllOpsToEnd(self, millis):
        for op in self.ops:
            t = op.getThread()
            if t is not None:
                try:
                    t.join(millis / 1000)
                except Exception as e:
                    Log.error("Failed to join a thread: " + e.getMessage())

    def newBucketOp(self, bucketName, bucketFolderName, serviceAccount, format, simpleFileName,
                    isTemp, overwrite, queueSize):
        opName = simpleFileName
        return BucketOp(opName, self, bucketName, bucketFolderName, serviceAccount, format, simpleFileName,
                        isTemp, overwrite, queueSize)

    def newCSVBucketOp(self, bucketName, bucketFolderName, serviceAccount, simpleFileName,
                       isTemp, overwrite, queueSize, columnNames: List[str]):
        return self.newCSVBucketOp(bucketName, bucketFolderName, serviceAccount, simpleFileName,
                                   isTemp, overwrite, CSVConst.DEFAULT_SEPARATOR_CHAR, columnNames,
                                   CSVConst.DEFAULT_COLUMN_NAME_LINE, queueSize)

    def newCSVBucketOp(self, bucketName, bucketFolderName, serviceAccount, simpleFileName,
                       isTemp, overwrite, separatorChar, columnNames: List[str],
                       columnNameLine, queueSize):
        opName = simpleFileName
        return BucketOp(opName, self, bucketName, bucketFolderName, serviceAccount, "csv", simpleFileName,
                        isTemp, overwrite, separatorChar, columnNames, columnNameLine, queueSize)
