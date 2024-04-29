import base64
import os
import tempfile
from moviepy.editor import VideoFileClip
from src.collager.pojo.ResultApi import Result
from src.collager.util import StorageApi, LogApi, DSApi
from src.collager.util.DLPApi import DLPApi
from src.collager.util.api import Api
import cv2
import numpy as np

bucket_name = StorageApi.getBucketName()


@Api(httpMethod="post")
def removeText(parameters):
    input_file_path = parameters.get('input_file')
    LogApi.auditLogInfo("File: " + input_file_path)
    content_type = parameters.get('content_type')
    file_id = parameters.get('file_id')
    action = parameters.get('action')
    extension = input_file_path.split(".")[1]

    file = StorageApi.readFromBucket(bucket_name, input_file_path)
    file_Data = file.getData()

    outputFolderLocal = tempfile.mkdtemp()
    if not os.path.isdir(outputFolderLocal):
        os.makedirs(outputFolderLocal)

    outputFilePath = os.path.join(outputFolderLocal, f"temp.{extension}")

    with open(outputFilePath, 'wb') as f:
        f.write(base64.b64decode(file_Data))

    info_type_names = [
        "ADVERTISING_ID", "AGE", "BLOOD_TYPE", "CREDIT_CARD_NUMBER",
        "CREDIT_CARD_TRACK_NUMBER", "COUNTRY_DEMOGRAPHIC", "DATE", "DATE_OF_BIRTH",
        "DOMAIN_NAME", "EMAIL_ADDRESS", "ETHNIC_GROUP", "FINANCIAL_ACCOUNT_NUMBER",
        "FIRST_NAME", "GENDER", "GENERIC_ID", "IBAN_CODE", "HTTP_COOKIE",
        "HTTP_USER_AGENT", "ICCID_NUMBER", "ICD9_CODE", "ICD10_CODE", "IMEI_HARDWARE_ID",
        "IMSI_ID", "IP_ADDRESS", "LAST_NAME", "LOCATION", "LOCATION_COORDINATES",
        "MAC_ADDRESS", "MAC_ADDRESS_LOCAL", "MARITAL_STATUS", "MEDICAL_RECORD_NUMBER",
        "MEDICAL_TERM", "ORGANIZATION_NAME", "PASSPORT", "PERSON_NAME", "PHONE_NUMBER",
        "STREET_ADDRESS", "SWIFT_CODE", "STORAGE_SIGNED_POLICY_DOCUMENT",
        "STORAGE_SIGNED_URL", "TIME", "URL", "VAT_NUMBER", "VEHICLE_IDENTIFICATION_NUMBER"
    ]

    try:
        video_clip = VideoFileClip(outputFilePath)

        def process_frame(frame):
            ret, buffer = cv2.imencode('.jpg', frame)
            base64_img = base64.b64encode(buffer.tobytes()).decode('utf-8')

            if action == "all":
                redacted_img = DLPApi.redactImageAllText(base64_img, "IMAGE_JPEG")
            elif action == "partial":
                redacted_img = DLPApi.redactImage(base64_img, "IMAGE_JPEG", info_type_names)
            else:
                return Result.getFailedResult("Invalid action")

            redacted_data = redacted_img['data']
            redacted_bytes = base64.b64decode(redacted_data.encode('utf-8'))
            # Convert the bytes data to an image
            redacted_image = cv2.imdecode(np.frombuffer(redacted_bytes, np.uint8), cv2.IMREAD_COLOR)

            return redacted_image

        processed_clip = video_clip.fl_image(process_frame)

        processed_clip.write_videofile(outputFilePath + f"_no_text.{extension}")

        f = open(outputFilePath + f"_no_text.{extension}", mode="rb")

        # Reading file data with read() method
        file_content = f.read()

        # Encode the content to Base64
        base64_string = base64.b64encode(file_content).decode("utf-8")

        # Delete the original file (not required)
        # StorageApi.deleteFileFromBucket(bucket_name, input_file_path)

        # Write the file to the bucket
        res = StorageApi.writeToBucket(
            bucket_name, base64_string, input_file_path, content_type)

        # Check the response for the new result including generation id.
        StorageApi.makePublic(bucket_name, input_file_path)

        # Update (Files table) with new generation id
        new_file_data = {
            "generation": res["data"]["generation"],
            "size": res["data"]["size"],
            "status": "Completed"
        }
        res2 = DSApi.updateUsingMap("File", file_id, new_file_data)

        return res2

    except FileNotFoundError as e:
        return Result.getFailedResult("Error: Input file not found. Please check the path. " + str(e))

    except Exception as e:  # Catch any unexpected errors
        return Result.getFailedResult("Failed to remove text:" + str(e))
