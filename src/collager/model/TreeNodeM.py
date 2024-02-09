from typing import List, Union

from src.collager.model.BaseM import BaseM
from src.collager.model.FileM import FileM


class TreeNodeM:
    def __init__(self):
        super().__init__()
        self.dirName: Union[str, None] = None
        self.children: List[BaseM] = []

    def getChildren(self) -> List[BaseM]:
        return self.children

    def setChildren(self, children: List[BaseM]) -> None:
        self.children = children

    def addChild(self, index: int, child: BaseM) -> None:
        self.children.insert(index, child)

    def addChild(self, child: BaseM) -> None:
        self.children.append(child)

    def getChild(self, name: str) -> Union[BaseM, None]:
        for base in self.children:
            if base.getName() == name:
                return base
        return None

    def getChildIgnoreCase(self, name: str) -> Union[BaseM, None]:
        for base in self.children:
            if base.getName().lower() == name.lower():
                return base
        return None

    def getChildFileM(self, name: str) -> Union[FileM, None]:
        m = self.getChild(name)
        if m is not None and isinstance(m, FileM):
            return m
        return None

    def getChildTreeNodeM(self, name: str) -> Union['TreeNodeM', None]:
        m = self.getChild(name)
        if m is not None and isinstance(m, TreeNodeM):
            return m
        return None

    def getUid(self) -> Union[str, None]:
        return self.uid

    def setUid(self, uid: Union[str, None]) -> None:
        self.uid = uid

    def getDirName(self) -> Union[str, None]:
        return self.dirName

    def setDirName(self, dirName: Union[str, None]) -> None:
        self.dirName = dirName
