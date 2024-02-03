from src.collager.util.HttpRequestUtil import HttpRequestUtil
from multimethods import multimethod
umBaseEndpoint = "/api/v1.1/um"

@multimethod()
def newUser():
    return HttpRequestUtil.post(umBaseEndpoint + "/currentUser", {})


def inviteUser(params):
    return HttpRequestUtil.post(umBaseEndpoint + "/inviteUser", params)


def editUser(userMap):
    return HttpRequestUtil.post(umBaseEndpoint + "/editUser", userMap)


def changePassword(user):
    return HttpRequestUtil.post(umBaseEndpoint + "/changePassword", user)


def resetPassword(user):
    return HttpRequestUtil.post(umBaseEndpoint + "/resetPassword", user)


def tenantOrg(org):
    return HttpRequestUtil.post(umBaseEndpoint + "/tenantOrg", org)


def currentUserTenantOrg():
    return HttpRequestUtil.get(umBaseEndpoint + "/currentUserTenantOrg")


def authState(params):
    return HttpRequestUtil.post(umBaseEndpoint + "/authState", params)


def contacts(params):
    return HttpRequestUtil.post(umBaseEndpoint + "/contacts", params)


def deleteUser(id):
    return HttpRequestUtil.delete(umBaseEndpoint + "/deleteUser?id=" + str(id))


def toggleSuspendActive(params):
    return HttpRequestUtil.post(umBaseEndpoint + "/toggleSuspendActive", params)


def getRoles():
    return HttpRequestUtil.get(umBaseEndpoint + "/getRoles")


def saveRole(role):
    return HttpRequestUtil.post(umBaseEndpoint + "/saveRole", role)


def deleteObject(roleName):
    return HttpRequestUtil.delete(umBaseEndpoint + "/deleteObject?roleName=" + roleName)


def switchUser(params):
    return HttpRequestUtil.post(umBaseEndpoint + "/switchUser", params)


def editMyProfile(userMap):
    return HttpRequestUtil.post(umBaseEndpoint + "/editMyProfile", userMap)


def changeMyPassword(user):
    return HttpRequestUtil.post(umBaseEndpoint + "/changeMyPassword", user)

@multimethod(dict)
def newUser(userMap):
    return HttpRequestUtil.post(umBaseEndpoint + "/newUser", userMap)


def editUser(userMap):
    return HttpRequestUtil.post(umBaseEndpoint + "/editUser", userMap)
