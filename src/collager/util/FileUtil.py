import os
import shutil
import tempfile
from typing import Optional

class FileUtil:
    @staticmethod
    def getNameWithoutExtension(fileName: str) -> str:
        return os.path.splitext(fileName)[0]

    @staticmethod
    def getFileExtension(fileName: str) -> str:
        return os.path.splitext(fileName)[1]

    @staticmethod
    def copyFile(inFile: str, outFile: str) -> None:
        shutil.copy2(inFile, outFile)

    @staticmethod
    def copyTextFile(file1: str, file2: str) -> None:
        shutil.copyfile(file1, file2)

    @staticmethod
    def renameTo(fromFile: str, toFile: str) -> None:
        os.rename(fromFile, toFile)

    @staticmethod
    def readFile(file: str, numberOfLines: Optional[int] = -1) -> str:
        with open(file, "r", encoding="utf-8") as f:
            if numberOfLines == -1:
                return f.read()
            else:
                return "".join([next(f) for _ in range(numberOfLines)])

    @staticmethod
    def writeFile(file: str, buf: str) -> None:
        with open(file, "w", encoding="utf-8") as f:
            f.write(buf)

    @staticmethod
    def getFileTimestamp(f: str) -> float:
        return os.path.getmtime(f)

    @staticmethod
    def isFileModifiedBefore(f: str, ts: float) -> bool:
        return FileUtil.getFileTimestamp(f) < ts

    @staticmethod
    def isFileModifiedBeforeDelta(f: str, ts: float, delta: float) -> bool:
        return ts - FileUtil.getFileTimestamp(f) > delta

    @staticmethod
    def getUniqueFileName(dirName: str, fileNamePrefix: str, ext: str = "") -> str:
        if ext and not ext.startswith("."):
            ext = "." + ext
        n = 1
        while True:
            fileName = f"{fileNamePrefix}-{n}{ext}"
            filePath = os.path.join(dirName, fileName)
            if not os.path.exists(filePath):
                break
            n += 1
        return fileName
