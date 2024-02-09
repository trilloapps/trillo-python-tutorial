from typing import Dict, Union


class SimpleSchema:
    def __init__(self):
        self.type: str = "object"
        self.array: bool = False
        self.required: bool = False
        self.exampleValue: Union[None, str, int, float, bool, dict, list] = None
        self.properties: Dict[str, SimpleSchema] = {}

    def getType(self) -> str:
        return self.type

    def setType(self, type: str) -> None:
        self.type = type

    def isArray(self) -> bool:
        return self.array

    def setArray(self, array: bool) -> None:
        self.array = array

    def getProperties(self) -> Dict:
        return self.properties

    def setProperties(self, properties: Dict) -> None:
        self.properties = properties

    def addProperty(self, name, property) -> None:
        self.properties[name] = property

    def isRequired(self) -> bool:
        return self.required

    def setRequired(self, required: bool) -> None:
        self.required = required

    def getExampleValue(self) -> Union[None, str, int, float, bool, dict, list]:
        return self.exampleValue

    def setExampleValue(self, exampleValue: Union[None, str, int, float, bool, dict, list]) -> None:
        self.exampleValue = exampleValue
