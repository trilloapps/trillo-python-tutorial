import logging
from typing import Dict, List

from src.collager.model.ClassM import ClassM
from src.collager.util import Util


class DataSourceM:
    def __init__(self):
        self.type: str = "unknown"
        self.properties: Dict[str, str] = {}
        self.classList: List[ClassM] = []
        self.orgName: str = ""
        self.appName: str = ""
        self.permitsDBCreate: bool = False
        self.custom: bool = False
        self.useDefault: bool = False
        self.unreachable: bool = False
        self.createMode: bool = False
        self.classMap: Dict[str, ClassM] = {}

    def getType(self) -> str:
        return self.type

    def setType(self, type: str):
        self.type = type

    def getProperties(self) -> Dict[str, str]:
        return self.properties

    def setProperties(self, properties: Dict[str, str]):
        self.properties = properties

    def getOrgName(self) -> str:
        return self.orgName

    def setOrgName(self, orgName: str):
        self.orgName = orgName

    def getAppName(self) -> str:
        return self.appName

    def setAppName(self, appName: str):
        self.appName = appName

    def isUseDefault(self) -> bool:
        return self.useDefault

    def setUseDefault(self, useDefault: bool):
        self.useDefault = useDefault

    def getClassList(self) -> List['ClassM']:
        return self.classList

    def addClassM(self, classM: 'ClassM'):
        if self.classMap.get(classM.getName()) is not None:
            self.deleteClassMFromListByName(classM.getName())
        self.classList.append(classM)
        self.classMap[classM.getName()] = classM

    def getClassM(self, name: str) -> 'ClassM':
        return self.classMap.get(name)

    def deleteClassMFromListByName(self, name: str):
        for i, classM in enumerate(self.classList):
            if name == classM.getName():
                del self.classList[i]
                return

    def isPermitsDBCreate(self) -> bool:
        return self.permitsDBCreate

    def setPermitsDBCreate(self, permitsDBCreate: bool):
        self.permitsDBCreate = permitsDBCreate

    def isCreateMode(self) -> bool:
        return self.createMode

    def setCreateMode(self, createMode: bool):
        self.createMode = createMode

    @staticmethod
    def mapToMetaData(map: Dict[str, object]) -> 'DataSourceM':
        dsM = Util.fromMap(map, DataSourceM)
        return dsM

    def isCustom(self) -> bool:
        return self.custom

    def setCustom(self, custom: bool):
        self.custom = custom

    def isUnreachable(self) -> bool:
        return self.unreachable

    def setUnreachable(self, unreachable: bool):
        self.unreachable = unreachable

    def getFullName(self) -> str:
        return (self.appName + "." if self.appName else "") + self.getName()
