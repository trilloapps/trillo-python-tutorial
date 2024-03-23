from multimethods import multimethod

from src.collager.util.BaseApi import BaseApi
from src.collager.util.Util import Util
from src.collager.util.HttpRequestUtil import HttpRequestUtil

folderBaseEndpoint = "/api/v1.1/foldersvc"


def getFullFolderTree(orderBy):
    res = HttpRequestUtil.get(folderBaseEndpoint + "/folders?orderBy=" + orderBy)
    return Util.convertToListOfDict(res)


def getHomeFolderTree(orderBy):
    res = HttpRequestUtil.get(folderBaseEndpoint + "/homeFolder?orderBy=" + orderBy)
    return Util.convertToDict(res)


def getHomeSubFolderTree(orderBy):
    res = HttpRequestUtil.get(folderBaseEndpoint + "/homeSubFolders?orderBy=" + orderBy)
    return Util.convertToListOfDict(res)


def getFolderAndFiles(folderId, orderBy, deleted):
    return HttpRequestUtil.get(
        folderBaseEndpoint + "/folderAndFiles?folderId=" + folderId + "&orderBy=" + orderBy + "&deleted=" + deleted)


def getSubFolders(folderId, orderBy):
    return HttpRequestUtil.get(folderBaseEndpoint + "/subFolders?folderId=" + folderId + "&orderBy=" + orderBy)


def getFolderParents(folderId):
    return HttpRequestUtil.get(folderBaseEndpoint + "/folderParents?folderId=" + folderId)


def getHomeFolderFiles(orderBy):
    return HttpRequestUtil.get(folderBaseEndpoint + "/home/files?orderBy=" + orderBy)


def getFolderTask(folderId):
    return HttpRequestUtil.get(folderBaseEndpoint + "/task?folderId=" + folderId)


def createFolder(folder):
    res = HttpRequestUtil.post(folderBaseEndpoint + "/folder/create", folder)
    return Util.convertToResult(res)


def createFolder(folder):
    res = HttpRequestUtil.post(folderBaseEndpoint + "/folder/create", folder)
    return Util.convertToResult(res)


def updateFolder(folder):
    res = HttpRequestUtil.post(folderBaseEndpoint + "/folder/update", folder)
    return Util.convertToResult(res)


def renameFolder(folderId, newName):
    body = {
        "folderId": folderId,
        "newName": newName
    }
    res = HttpRequestUtil.post(folderBaseEndpoint + "/folder/rename", body)
    return Util.convertToResult(res)


def moveFolder(folderId, newParentId):
    body = {
        "folderId": folderId,
        "newParentId": newParentId
    }
    res = HttpRequestUtil.post(folderBaseEndpoint + "/folder/move", body)
    return Util.convertToResult(res)


def deleteFolder(folderId):
    body = {
        "folderId": folderId
    }
    res = HttpRequestUtil.post(folderBaseEndpoint + "/folder/delete", body)
    return Util.convertToResult(res)


def deleteGroup(groupId):
    body = {
        "groupId": groupId
    }
    res = HttpRequestUtil.post(folderBaseEndpoint + "/group/delete", body)
    return Util.convertToResult(res)


def deleteGroup(groupId):
    body = {
        "groupId": groupId
    }
    res = HttpRequestUtil.post(folderBaseEndpoint + "/group/delete", body)
    return Util.convertToResult(res)


def createUploadSignedUrl(folderId, duration=None):
    body = {
        "folderId": folderId,
        "duration": duration
    }
    res = HttpRequestUtil.post(folderBaseEndpoint + "/folder/createUploadSignedUrl", body)
    return Util.convertToResult(res)


def createDownloadSignedUrl(id, baseUri=None, duration=None):
    if baseUri is None:
        body = {
            "id": id,
            "duration": duration
        }
    else:
        body = {
            "id": id,
            "duration": duration,
            "baseUri": baseUri
        }
    res = HttpRequestUtil.post(folderBaseEndpoint + "/folder/delete", body)
    return Util.convertToResult(res)


def renameFile(fileId, newName):
    body = {
        "fileId": fileId,
        "newName": newName
    }
    res = HttpRequestUtil.post(folderBaseEndpoint + "/file/rename", body)
    return Util.convertToResult(res)


def moveFile(fileId, newParentFolderId):
    body = {
        "fileId": fileId,
        "newParentFolderId": newParentFolderId
    }
    res = HttpRequestUtil.post(folderBaseEndpoint + "/file/move", body)
    return Util.convertToResult(res)


def deleteFile(fileId):
    body = {
        "fileId": fileId
    }
    res = HttpRequestUtil.post(folderBaseEndpoint + "/file/delete", body)
    return Util.convertToResult(res)


def deleteFile2(fileId, folderName):
    body = {
        "fileId": fileId,
        "folderName": folderName
    }
    res = HttpRequestUtil.post(folderBaseEndpoint + "/file/delete2", body)
    return Util.convertToResult(res)


def deleteManyFiles(ids):
    body = {
        "ids": ids
    }
    res = HttpRequestUtil.post(folderBaseEndpoint + "/file/deleteMany", body)
    return Util.convertToResult(res)


def restoreManyFiles(ids, keepId):
    body = {
        "ids": ids
    }
    res = HttpRequestUtil.post(folderBaseEndpoint + "/file/restoreMany?keepId=" + keepId, body)
    return Util.convertToResult(res)


def copyFile(fileId, newParentFolderId, newName):
    body = {
        "fileId": fileId,
        "newParentFolderId": newParentFolderId,
        "newName": newName
    }
    res = HttpRequestUtil.post(folderBaseEndpoint + "/file/copy", body)
    return Util.convertToResult(res)


def shareFile(fileId, targetFolderPath, idOfUserToShareWith):
    body = {
        "fileId": fileId,
        "targetFolderPath": targetFolderPath,
        "idOfUserToShareWith": idOfUserToShareWith
    }
    res = HttpRequestUtil.post(folderBaseEndpoint + "/file/share", body)
    return Util.convertToResult(res)


def assignFile(fileId, idOfUserToAssign):
    body = {
        "fileId": fileId,
        "idOfUserToAssign": idOfUserToAssign
    }
    res = HttpRequestUtil.post(folderBaseEndpoint + "/file/assign", body)
    return Util.convertToResult(res)


def updateStatus(fileId, status):
    return BaseApi.remoteCall("FolderApi", "updateStatus", int(fileId), str(status))


def saveFileObject(params):
    return HttpRequestUtil.post(folderBaseEndpoint + "/folder/saveFileObject", params)


def saveFileObjectWithTask(params):
    return HttpRequestUtil.post(folderBaseEndpoint + "/folder/saveFileObjectWithTask", params)


def saveFileObjectWithFunction(params):
    return HttpRequestUtil.post(folderBaseEndpoint + "/folder/saveFileObjectWithFunction", params)


@multimethod(dict)
def retrieveSignedUrl(params):
    return HttpRequestUtil.post(folderBaseEndpoint + "/folder/retieveSignedUrl", params)


def saveFileGetSignedUrl(params):
    return HttpRequestUtil.post(folderBaseEndpoint + "/folder/saveFileGetSignedUrl", params)


def retrieveSignedUrlPublic(params):
    return HttpRequestUtil.post(folderBaseEndpoint + "/retrieveSignedUrlPublic", params)


def saveFolderTask(params):
    return HttpRequestUtil.post(folderBaseEndpoint + "/task", params)


def search(params):
    return HttpRequestUtil.post(folderBaseEndpoint + "/search", params)


def autoComplete(params):
    return HttpRequestUtil.post(folderBaseEndpoint + "/autoComplete", params)


def isBusy(providerName):
    return HttpRequestUtil.post(folderBaseEndpoint + "/" + providerName + "/folder/isBusy", {})


def startFullSyncTask(providerName):
    return HttpRequestUtil.post(folderBaseEndpoint + "/" + providerName + "/folder/fullSync", {})


def syncFolder(folderId):
    return BaseApi.remoteCallAsResult("FolderApi", "syncFolder", folderId)


def getCreateGroupFolderWithFiles(path):
    return BaseApi.remoteCall("FolderApi", "getCreateGroupFolderWithFiles", str(path))



def retrieveManyUploadSignedUrls(bucket, folderName, subFolder, folderId, fileNames, contentType, duration,
                                 functionName, functionParams):
    body = {
        "bucket": bucket,
        "folderName": folderName,
        "subFolder": subFolder,
        "folderId": folderId,
        "fileNames": fileNames,
        "contentType": contentType,
        "duration": duration,
        "functionName": functionName,
        "functionParams": functionParams

    }
    res = HttpRequestUtil.post(folderBaseEndpoint + "/folder/retrieveManyUploadSignedUrls", body)
    return Util.convertToResult(res)


@multimethod(str, str, str, str, str, str, bool, int)
def retrieveSignedUrl(id, folderName, subFolder, folderId, fileName, contentType, asAttachment,
                      duration):
    body = {
        "id": id,
        "folderName": folderName,
        "subFolder": subFolder,
        "folderId": folderId,
        "fileName": fileName,
        "contentType": contentType,
        "asAttachment": asAttachment,
        "duration": duration

    }
    res = HttpRequestUtil.post(folderBaseEndpoint + "/folder/retrieveSignedUrl", body)
    return Util.convertToResult(res)
