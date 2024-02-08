from typing import Dict


class DSSQLTemplate:
    def __init__(self):
        self.name: str = ""
        self.sql: str = ""
        self.skipTenantCheck: bool = False

    def getName(self) -> str:
        return self.name

    def setName(self, name: str) -> None:
        self.name = name

    def getSql(self) -> str:
        return self.sql

    def setSql(self, sql: str) -> None:
        self.sql = sql

    def isSkipTenantCheck(self) -> bool:
        return self.skipTenantCheck

    def setSkipTenantCheck(self, skipTenantCheck: bool) -> None:
        self.skipTenantCheck = skipTenantCheck

    @staticmethod
    def mapToMetaData(mapData: Dict[str, object]) -> 'DSSQLTemplate':
        template = DSSQLTemplate()
        template.name = mapData.get("name", "")
        template.sql = mapData.get("sql", "")
        template.skipTenantCheck = mapData.get("skipTenantCheck", False)
        return template
