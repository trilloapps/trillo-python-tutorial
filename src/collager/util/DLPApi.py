from src.collager.util.BaseApi import BaseApi
from src.collager.util.HttpRequestUtil import HttpRequestUtil
dlpBaseEndpoint = "/api/v1.1/dlp"

class DLPApi:
    @staticmethod
    def inspect(text, informationTypes):
        return BaseApi.remoteCallAsResult("DLPApi", "inspect", text, informationTypes)

    @staticmethod
    def redactImage(base64String, imageType, informationType):
        body = {"base64String": base64String,
                "imageType": imageType,
                "informationType": informationType}
        return HttpRequestUtil.post(dlpBaseEndpoint + "/redactImage", body)


    @staticmethod
    def redactImageAllText(base64String, imageType):
        body = {"base64String": base64String,
                "imageType": imageType}
        return HttpRequestUtil.post(dlpBaseEndpoint + "/redactImageAllText", body)

    @staticmethod
    def redactPII(text):
        return BaseApi.remoteCallAsResult("DLPApi", "redactPII", text)

    class ImageType:
        BYTES_TYPE_UNSPECIFIED = "BYTES_TYPE_UNSPECIFIED"
        IMAGE = "IMAGE"
        IMAGE_JPEG = "IMAGE_JPEG"
        IMAGE_BMP = "IMAGE_BMP"
        IMAGE_PNG = "IMAGE_PNG"
        IMAGE_SVG = "IMAGE_SVG"
        TEXT_UTF8 = "TEXT_UTF8"
        WORD_DOCUMENT = "WORD_DOCUMENT"
        PDF = "PDF"
        POWERPOINT_DOCUMENT = "POWERPOINT_DOCUMENT"
        EXCEL_DOCUMENT = "EXCEL_DOCUMENT"
        AVRO = "AVRO"
        CSV = "CSV"
        TSV = "TSV"
