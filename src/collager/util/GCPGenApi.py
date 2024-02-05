from typing import List, Union, Dict

from src.collager.util import Util

try:
  from src.io.RunFunction import Proxy
except:
  from src.io.util.Proxy import Proxy

class GCPGenApi():

    @staticmethod
    def chat(params: Dict[str, Union[str, int]]) -> object:
        return Proxy.remoteCall("GCPGenApi", "chat", params)

    @staticmethod
    def summarizeText(text: str) -> 'Result':
        res = Proxy.remoteCall("GCPGenApi", "summarizeText", text)
        return Util.convertToResult(res)

    @staticmethod
    def classifyText(inputClasses: List[str], text: str) -> 'Result':
        return Proxy.remoteCallAsResult("GCPGenApi", "classifyText", inputClasses, text)

    @staticmethod
    def ams(text: str) -> 'Result':
        return Proxy.remoteCallAsResult("GCPGenApi", "ams", text)

    @staticmethod
    def generateEmbedding(text: str) -> 'Result':
        return Proxy.remoteCallAsResult("GCPGenApi", "generateEmbedding", text)

    @staticmethod
    def generateImageInBucket(prompt: str, imageCount: int, outputGcsUriFolder: str) -> 'Result':
        return Proxy.remoteCallAsResult("GCPGenApi", "generateImageInBucket", prompt, imageCount, outputGcsUriFolder)

    @staticmethod
    def generateImageAsByte(prompt: str, imageCount: int) -> 'Result':
        return Proxy.remoteCallAsResult("GCPGenApi", "generateImageAsByte", prompt, imageCount)

    @staticmethod
    def generateCode(prompt: str) -> 'Result':
        return Proxy.remoteCallAsResult("GCPGenApi", "generateCode", prompt)

    @staticmethod
    def text(prompt: str) -> 'Result':
        return Proxy.remoteCallAsResult("GCPGenApi", "text", prompt)

    @staticmethod
    def extractEntitiesFromTextList(prompt: str, texts: List[str]) -> 'Result':
        return Proxy.remoteCallAsResult("GCPGenApi", "extractEntitiesFromTextList", prompt, texts)

    @staticmethod
    def extractEntitiesFromText(prompt: str, text: str) -> 'Result':
        return Proxy.remoteCallAsResult("GCPGenApi", "extractEntitiesFromText", prompt, text)
