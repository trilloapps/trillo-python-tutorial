from src.collager.util.BaseApi import BaseApi


class DLPApi:
    @staticmethod
    def inspect(text, informationTypes):
        return BaseApi.remoteCallAsResult("DLPApi", "inspect", text, informationTypes)

    @staticmethod
    def redactImage(base64String, imageType, informationType):
        return BaseApi.remoteCallAsResult("DLPApi", "redactImage", base64String, imageType, informationType)

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
