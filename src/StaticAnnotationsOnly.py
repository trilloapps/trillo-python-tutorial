from src.collager.util.api import Api
import base64
import os
import tempfile
from moviepy.editor import VideoFileClip
from src.collager.pojo.ResultApi import Result
from src.collager.util import StorageApi, LogApi, DSApi
from src.collager.util.DLPApi import DLPApi
import cv2
import numpy as np

bucket_name = StorageApi.getBucketName()


@Api(httpMethod="post")
def testing(parameters):
    input_file_path = parameters.get('input_file')
    LogApi.auditLogInfo("File: " + input_file_path)
    content_type = parameters.get('content_type')
    file_id = parameters.get('file_id')
    startTime = parameters.get('startTime')
    endTime = parameters.get('endTime')
    shape = parameters.get('shape')
    extension = input_file_path.split(".")[1]

    file = StorageApi.readFromBucket(bucket_name, input_file_path)
    file_Data = file.getData()

    outputFolderLocal = tempfile.mkdtemp()
    if not os.path.isdir(outputFolderLocal):
        os.makedirs(outputFolderLocal)

    outputFilePath = os.path.join(outputFolderLocal, f"temp.{extension}")

    with open(outputFilePath, 'wb') as f:
        f.write(base64.b64decode(file_Data))

    # video_path = '/Users/danialaslam/Documents/trillo-python-tutorial/src/text.mp4'
    # output_path = '/Users/danialaslam/Documents/trillo-python-tutorial/src/staticannotation.mp4'
    # Load the video

    try:
        cap = cv2.VideoCapture(outputFilePath)
        # Get the video properties
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        start_x, start_y = 100, 200
        end_x, end_y = 300, 400
        font = cv2.FONT_HERSHEY_SIMPLEX

        # Define the codec and create VideoWriter object

        fourcc = cv2.VideoWriter_fourcc(*'h264')
        out = cv2.VideoWriter(outputFilePath + f"_no_text.{extension}", fourcc, fps, (frame_width, frame_height))

        # Loop through each frame
        while cap.isOpened():

            ret, frame = cap.read()
            if not ret:
                break

            cv2.rectangle(frame, (start_x + 300, start_y + 300), (end_x + 300, end_y + 300), (0, 25, 125), thickness=-1)
            cv2.arrowedLine(frame, (start_x + 225, start_y), (end_x + 225, end_y), (0, 25, 125), thickness=25)
            cv2.circle(frame, (start_x + 50, start_y + 100), 100, (0, 25, 125), thickness=10)
            cv2.putText(frame, 'TEXT ON VIDEO', (150, 150), font, 4, (0, 25, 125), 15, cv2.LINE_4)
            cv2.imshow('Annotated Video', frame)
            # Write the annotated frame
            out.write(frame)

        # Release everything when done
        cap.release()
        out.release()

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
