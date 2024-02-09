from typing import Dict

class RuntimeContext:
    def __init__(self):
        self.idOfUser = 0
        self.userId = "guest"
        self.firstName = ""
        self.lastName = ""
        self.email = ""
        self.externalId = ""
        self.role = ""
        self.userOrgName = ""
        self.emailVerified = False
        self.tenantId = ""
        self.tenantName = ""
        self.userOrgId = 0
        self.pictureUrl = ""
        self.orgName = ""
        self.appName = ""
        self.taskName = ""
        self.executionId = -1
        self.mobilePhone = None
        self.v = {}

    def getFullName(self) -> str:
        if self.firstName or self.lastName:
            return f"{self.firstName} {self.lastName}".strip()
        return self.userId

    def toMap(self) -> Dict[str, object]:
        return {
            "idOfUser": self.idOfUser,
            "userId": self.userId,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            "orgName": self.orgName,
            "appName": self.appName,
            "externalId": self.externalId,
            "role": self.role,
            "userOrgName": self.userOrgName,
            "emailVerified": self.emailVerified,
            "tenantId": self.tenantId,
            "tenantName": self.tenantName,
            "userOrgId": self.userOrgId,
            "pictureUrl": self.pictureUrl,
            "v": self.v,
            "taskName": self.taskName,
            "executionId": self.executionId
        }
