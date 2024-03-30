from typing import List, Union, Dict

from src.collager.util.BaseApi import BaseApi
from src.collager.util.Util import Util
from src.io.util.Proxy import Proxy


class GCPGenApi:

    @staticmethod
    def chat(params: Dict[str, Union[str, int]]) -> object:
        return Proxy.remoteCall("GCPGenApi", "chat", params)

    @staticmethod
    def summarizeText(text: str) -> 'Result':
        return BaseApi.remoteCallAsResult("GCPGenApi", "summarizeText", text)

    @staticmethod
    def classifyText(inputClasses: List[str], text: str) -> 'Result':
        return BaseApi.remoteCallAsResult("GCPGenApi", "classifyText", inputClasses, text)

    @staticmethod
    def ams(text: str) -> 'Result':
        return BaseApi.remoteCallAsResult("GCPGenApi", "ams", text)

    @staticmethod
    def generateEmbedding(text: str) -> 'Result':
        return BaseApi.remoteCallAsResult("GCPGenApi", "generateEmbedding", text)

    @staticmethod
    def generateImageInBucket(prompt: str, imageCount: int, outputGcsUriFolder: str) -> 'Result':
        return BaseApi.remoteCallAsResult("GCPGenApi", "generateImageInBucket", prompt, imageCount, outputGcsUriFolder)

    @staticmethod
    def generateImageAsByte(prompt: str, imageCount: int) -> 'Result':
        return BaseApi.remoteCallAsResult("GCPGenApi", "generateImageAsByte", prompt, imageCount)

    @staticmethod
    def generateCode(prompt: str) -> 'Result':
        return BaseApi.remoteCallAsResult("GCPGenApi", "generateCode", prompt)
    

    @staticmethod
    def text(prompt: str) -> 'Result':
        return BaseApi.remoteCallAsResult("GCPGenApi", "text", prompt)

    @staticmethod
    def extractEntitiesFromTextList(prompt: str, texts: List[str]) -> 'Result':
        return BaseApi.remoteCallAsResult("GCPGenApi", "extractEntitiesFromTextList", prompt, texts)

    @staticmethod
    def extractEntitiesFromText(prompt: str, text: str) -> 'Result':
        return BaseApi.remoteCallAsResult("GCPGenApi", "extractEntitiesFromText", prompt, text)

    @staticmethod
    def vertexAiGetAnswer(question: str, datastoreId: str) -> 'Object':
        return BaseApi.remoteCall("GCPGenApi", "vertexAiGetAnswer", question, datastoreId)

    @staticmethod
    def vertexAiGetAnswer(question: str, datastoreId: str, pageSize: int, modelVersion: str) -> 'Object':
        return BaseApi.remoteCall("GCPGenApi", "vertexAiGetAnswer", question, datastoreId, pageSize, modelVersion)
