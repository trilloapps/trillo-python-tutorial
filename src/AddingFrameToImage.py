from src.collager.util.api import Api
import base64
import os
import tempfile
from src.collager.pojo.ResultApi import Result
from src.collager.util import StorageApi, LogApi, DSApi
import cv2
import numpy as np

# Load the video
bucket_name = StorageApi.getBucketName()


@Api(httpMethod="post")
def testing(parameters):
    # input_file_path = parameters.get('input_file')
    input_file_path = "text.mp4"
    # input_image_path = parameters.get('input_image')
    input_image_path = "dicom1.jpeg"
    # LogApi.auditLogInfo("File: " + input_file_path)
    # content_type = parameters.get('content_type')
    content_type = "video/mp4"
    file_id = parameters.get('file_id')
    # startTime = parameters.get('startTime')
    # endTime = parameters.get('endTime')
    extension = input_file_path.split(".")[1]

    file = StorageApi.readFromBucket(bucket_name, input_file_path)
    file_Data = file.getData()

    outputFolderLocal = tempfile.mkdtemp()
    if not os.path.isdir(outputFolderLocal):
        os.makedirs(outputFolderLocal)

    outputFilePath = os.path.join(outputFolderLocal, f"temp.{extension}")

    with open(outputFilePath, 'wb') as f:
        f.write(base64.b64decode(file_Data))

    LogApi.auditLogInfo("VIDEO FILE OPENED")

    # Load the image to add
    image = StorageApi.readFromBucket(bucket_name, input_image_path)
    image_Data = image.getData()
    imageFilePath = os.path.join(outputFolderLocal, f"tempimage.{extension}")

    with open(imageFilePath, 'wb') as foo:
        foo.write(base64.b64decode(image_Data))

    LogApi.auditLogInfo("Image FILE OPENED")

    try:
        cap = cv2.VideoCapture(outputFilePath)

        # Get the video properties
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Desired timestamp to add the image (in seconds)
        start_timestamp = 2
        end_timestamp = 6
        fourcc = cv2.VideoWriter_fourcc(*'avc1')
        out = cv2.VideoWriter(outputFilePath + f"_no_text.{extension}", fourcc, fps, (frame_width, frame_height))

        # Read frames until the desired timestamp
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Get the current timestamp
            current_timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0

            # Check if we've reached the desired timestamp
            # if start_timestamp <= current_timestamp <= end_timestamp:
            if current_timestamp >= start_timestamp and current_timestamp <= end_timestamp:

                image_with_alpha = cv2.imread(imageFilePath)

                if image_with_alpha.shape[2] == 4:
                    image = cv2.cvtColor(image_with_alpha, cv2.COLOR_BGRA2BGR)
                else:
                    image = image_with_alpha

                # Resize the image to fit the frame
                image = cv2.resize(image, (frame_width, frame_height))

                # You can adjust the position of the image as per your requirements
                x_offset = 0  # adjust the x offset
                y_offset = 0  # adjust the y offset
                frame[y_offset:y_offset + image.shape[0], x_offset:x_offset + image.shape[1]] = image

            out.write(frame)

        # Release everything when done
        LogApi.auditLogInfo("Outside Loop")
        cap.release()
        out.release()
        LogApi.auditLogInfo("Opening modified file")
        f = open(outputFilePath + f"_no_text.{extension}", mode="rb")
        LogApi.auditLogInfo("File Opened")
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

        LogApi.auditLogInfo("File modified on bucket Successfully")

        # Update (Files table) with new generation id
        # new_file_data = {
        #     "generation": res["data"]["generation"],
        #     "size": res["data"]["size"],
        #     "status": "Completed"
        # }
        # res2 = DSApi.updateUsingMap("File", file_id, new_file_data)

        return res

    except FileNotFoundError as e:
        return Result.getFailedResult("Error: Input file not found. Please check the path. " + str(e))

    except Exception as e:  # Catch any unexpected errors
        return Result.getFailedResult("Failed to remove text:" + str(e))
