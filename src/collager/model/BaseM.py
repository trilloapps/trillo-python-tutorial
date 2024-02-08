from typing import Dict, Any


class BaseM:

    def __init__(self):
        self.id = None
        self.name = None
        self.displayName = None
        self.description = None
        self.securityPolicies = None
        self.errored = False
        self.message = None
        self.props = None

    def getId(self) -> str:
        return self.id

    def setId(self, id: str) -> None:
        self.id = id

    def getName(self) -> str:
        return self.name

    def setName(self, name: str) -> None:
        self.name = name

    def getDisplayName(self) -> str:
        return self.displayName

    def setDisplayName(self, displayName: str) -> None:
        self.displayName = displayName

    def getDescription(self) -> str:
        return self.description

    def setDescription(self, description: str) -> None:
        self.description = description

    def getSecurityPolicies(self) -> str:
        return self.securityPolicies

    def setSecurityPolicies(self, securityPolicies: str) -> None:
        self.securityPolicies = securityPolicies

    def getProps(self) -> Dict[str, Any]:
        return self.props

    def setProps(self, props: Dict[str, Any]) -> None:
        self.props = props

    def setProp(self, name: str, value: Any) -> None:
        if self.props is None:
            self.props = {}
        self.props[name] = value

    def getProp(self, name: str) -> Any:
        if self.props:
            return self.props.get(name)
        return None

    def removeProp(self, name: str) -> Any:
        if self.props:
            return self.props.pop(name, None)
        return None

    def isErrored(self) -> bool:
        return self.errored

    def setErrored(self, errored: bool) -> None:
        self.errored = errored

    def getMessage(self) -> str:
        return self.message

    def setMessage(self, message: str) -> None:
        self.message = message

    def addMessage(self, message: str) -> None:
        if self.message is None:
            self.message = message
        else:
            self.message += "\n" + message
