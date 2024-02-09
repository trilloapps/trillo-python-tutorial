from typing import Optional


class FileM:
    def __init__(self):
        self.fileName: Optional[str] = None
        self.content: Optional[str] = None
        self.size: int = 0
        self.lastModified: int = 0
        self.url: Optional[str] = None

        self.modelClassName: Optional[str] = None
        self.uid: Optional[str] = None
        self.folder: Optional[str] = None

    def getFileName(self) -> Optional[str]:
        return self.fileName

    def setFileName(self, fileName: Optional[str]) -> None:
        if fileName is not None:
            self.fileName = fileName.replace("\\", "/")
        else:
            self.fileName = None

    def getContent(self) -> Optional[str]:
        return self.content

    def setContent(self, content: Optional[str]) -> None:
        self.content = content

    def getUid(self) -> Optional[str]:
        return self.uid

    def setUid(self, uid: Optional[str]) -> None:
        self.uid = uid

    def getModelClassName(self) -> Optional[str]:
        return self.modelClassName

    def setModelClassName(self, modelClassName: Optional[str]) -> None:
        self.modelClassName = modelClassName

    def getSize(self) -> int:
        return self.size

    def setSize(self, size: int) -> None:
        self.size = size

    def getLastModified(self) -> int:
        return self.lastModified

    def setLastModified(self, lastModified: int) -> None:
        self.lastModified = lastModified

    def getUrl(self) -> Optional[str]:
        return self.url

    def setUrl(self, url: Optional[str]) -> None:
        self.url = url

    def getFolder(self) -> Optional[str]:
        return self.folder

    def setFolder(self, folder: Optional[str]) -> None:
        self.folder = folder
