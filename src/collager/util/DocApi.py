from multimethods import multimethod
from src.collager.util.Util import Util
from src.collager.util.HttpRequestUtil import HttpRequestUtil

docBaseEndpoint = "/api/v1.1/docsvc"


def getFolders():
    res = HttpRequestUtil.get(docBaseEndpoint + "/folders")
    return Util.convertToListOfDict(res)


def getDocFolderAndDocList(folderId, orderBy, deleted):
    return HttpRequestUtil.get(
        docBaseEndpoint + "/foldersAndDocs?folderId=" + folderId + "&orderBy=" + orderBy + "&deleted=" + deleted)


def listHITLDocs(folderId, orderBy, deleted):
    return HttpRequestUtil.get(
        docBaseEndpoint + "/listHITLDocs?folderId=" + folderId + "&orderBy=" + orderBy + "&deleted=" + deleted)


def getDocFolderList(folderId, orderBy):
    res = HttpRequestUtil.get(docBaseEndpoint + "/subFolders?folderId=" + folderId + "&orderBy=" + orderBy)
    return Util.convertToListOfDict(res)


def getDocFolderParents(folderId):
    return HttpRequestUtil.get(docBaseEndpoint + "/foldefParents?folderId=" + folderId)


def getHomeFolderFiles(folderId, orderBy):
    res = HttpRequestUtil.get(docBaseEndpoint + "/docs?folderId=" + folderId + "&orderBy=" + orderBy)
    return Util.convertToListOfDict(res)


def getDocAISchema(schemaDisplayName):
    return HttpRequestUtil.get(docBaseEndpoint + "/getDocAISchema?schemaDisplayName=" + schemaDisplayName)


def getDocAIDocument(docId):
    return HttpRequestUtil.get(docBaseEndpoint + "/docs?docId=" + docId)


def getDocAIResult(docId):
    return HttpRequestUtil.get(docBaseEndpoint + "/docAIResult?docId=" + docId)


def getDocAIResults(folderId, start, pageSize):
    return HttpRequestUtil.get(
        docBaseEndpoint + "/docAIResults?folderId=" + folderId + "&start=" + start + "&pageSize=" + pageSize)


def getSummaryResult(docId):
    return HttpRequestUtil.get(docBaseEndpoint + "/summary?docId=" + docId)


def getSummaryResults(folderId, start, pageSize):
    return HttpRequestUtil.get(
        docBaseEndpoint + "/summaries?folderId=" + folderId + "&start=" + start + "&pageSize=" + pageSize)


def createDocFolder(folder):
    body = {
        "folder": folder
    }
    res = HttpRequestUtil.post(docBaseEndpoint + "/folder/create", body)
    return Util.convertToResult(res)


def updateFolder(folder):
    body = {
        "folder": folder
    }
    res = HttpRequestUtil.post(docBaseEndpoint + "/folder/update", body)
    return Util.convertToResult(res)


def updateDocFolderProperties(params):
    res = HttpRequestUtil.post(docBaseEndpoint + "/folder/updateDocFolderProperties", params)
    return Util.convertToResult(res)


def renameDocFolder(folderId, newName):
    body = {
        "folderId": folderId,
        "newName": newName
    }
    res = HttpRequestUtil.post(docBaseEndpoint + "/folder/rename", body)
    return Util.convertToResult(res)


def moveDocFolder(folderId, newParentId):
    body = {
        "folderId": folderId,
        "newParentId": newParentId
    }
    res = HttpRequestUtil.post(docBaseEndpoint + "/folder/move", body)
    return Util.convertToResult(res)


def deleteDocFolder(folderId):
    body = {
        "folderId": folderId
    }
    res = HttpRequestUtil.post(docBaseEndpoint + "/folder/delete", body)
    return Util.convertToResult(res)


@multimethod(str, int)
def createUploadSignedUrl(folderId, duration):
    body = {
        "folderId": folderId,
        "duration": duration
    }
    res = HttpRequestUtil.post(docBaseEndpoint + "/folder/createUploadSignedUrl", body)
    return Util.convertToResult(res)


@multimethod(str)
def createUploadSignedUrl(folderId):
    body = {
        "folderId": folderId
    }
    res = HttpRequestUtil.post(docBaseEndpoint + "/folder/createUploadSignedUrl", body)
    return Util.convertToResult(res)


@multimethod(str)
def createDownloadSignedUrl(folderId):
    body = {
        "folderId": folderId
    }
    res = HttpRequestUtil.post(docBaseEndpoint + "/folder/createDownloadSignedUrl", body)
    return Util.convertToResult(res)


@multimethod(str, int)
def createDownloadSignedUrl(folderId, duration):
    body = {
        "folderId": folderId,
        "duration": duration
    }
    res = HttpRequestUtil.post(docBaseEndpoint + "/folder/createDownloadSignedUrl", body)
    return Util.convertToResult(res)


def renameDoc(docId, newName):
    body = {
        "docId": docId,
        "newName": newName
    }
    res = HttpRequestUtil.post(docBaseEndpoint + "/docsvc/rename", body)
    return Util.convertToResult(res)


def moveDoc(docId, newParentFolderId):
    body = {
        "docId": docId,
        "newParentFolderId": newParentFolderId
    }
    res = HttpRequestUtil.post(docBaseEndpoint + "/docsvc/move", body)
    return Util.convertToResult(res)


def deleteDoc(docId):
    body = {
        "docId": docId
    }
    res = HttpRequestUtil.post(docBaseEndpoint + "/docsvc/delete", body)
    return Util.convertToResult(res)


def deleteManyDocs(ids, permanent):
    body = {
        "ids": ids,
        "permanent": permanent
    }
    res = HttpRequestUtil.post(docBaseEndpoint + "/docsvc/deleteMany", body)
    return Util.convertToResult(res)


def restoreManyDocs(ids):
    body = {
        "ids": ids
    }
    res = HttpRequestUtil.post(docBaseEndpoint + "/docsvc/restoreMany", body)
    return Util.convertToResult(res)


def copyDoc(docId, newParentFolderId, newName):
    body = {
        "docId": docId,
        "newParentFolderId": newParentFolderId,
        "newName": newName
    }
    res = HttpRequestUtil.post(docBaseEndpoint + "/docsvc/copy", body)
    return Util.convertToResult(res)


def saveDocObject(params):
    return HttpRequestUtil.post(docBaseEndpoint + "/folder/saveDocObject", params)


def updateDocProperties(params):
    res = HttpRequestUtil.post(docBaseEndpoint + "/docsvc/updateDocProperties", params)
    return Util.convertToResult(res)


def retrieveSignedUrl(docId, contentType, asAttachment, duration):
    body = {
        "docId": docId,
        "contentType": contentType,
        "asAttachment": asAttachment,
        "duration": duration
    }
    res = HttpRequestUtil.post(docBaseEndpoint + "/folder/retrieveSignedUrl", body)
    return Util.convertToResult(res)


def retrieveUploadSignedUrl(folderId, fileName, contentType):
    body = {
        "folderId": folderId,
        "fileName": fileName,
        "contentType": contentType
    }
    res = HttpRequestUtil.post(docBaseEndpoint + "/folder/retrieveSignedUrl", body)
    return Util.convertToResult(res)


def saveDocGetSignedUrl(params):
    return HttpRequestUtil.post(docBaseEndpoint + "/folder/saveDocGetSignedUrl", params)


def autoComplete(params):
    return HttpRequestUtil.post(docBaseEndpoint + "/docsvc/autoComplete", params)


def search(params):
    return HttpRequestUtil.post(docBaseEndpoint + "/docsvc/search", params)


def executeWorkflow(params):
    return HttpRequestUtil.post(docBaseEndpoint + "/docsvc/executeWorkflow", params)


def createDocAIDocument(params):
    return HttpRequestUtil.post(docBaseEndpoint + "/docsvc/createDocAIDocument", params)


def summarizeDocs(params):
    return HttpRequestUtil.post(docBaseEndpoint + "/docsvc/summarizeDocs", params)


def extractEntities(params):
    return HttpRequestUtil.post(docBaseEndpoint + "/docsvc/extractEntities", params)


def chat(params):
    return HttpRequestUtil.post(docBaseEndpoint + "/docsvc/chat", params)


def generateJson(params):
    return HttpRequestUtil.post(docBaseEndpoint + "/docsvc/generateJson", params)


def bulkUpload(params):
    return HttpRequestUtil.post(docBaseEndpoint + "/docsvc/bulkUpload", params)


def deleteDocAIDocument(docId):
    return HttpRequestUtil.delete(docBaseEndpoint + "/docsvc/deleteDocAIDocument?docId=" + docId)


def deleteDocAISchema(schemaDisplayName):
    return HttpRequestUtil.delete(docBaseEndpoint + "/docsvc/deleteDocAISchema?schemaDisplayName=" + schemaDisplayName)
