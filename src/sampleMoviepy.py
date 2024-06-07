from src.collager.util.api import Api
import base64
import os
import tempfile
from src.collager.pojo.ResultApi import Result
from src.collager.util import StorageApi, LogApi, DSApi
from moviepy.editor import VideoFileClip, ImageClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
import cv2

import numpy as np

# Load the video
bucket_name = StorageApi.getBucketName()


@Api(httpMethod="post")
def testing(parameters):
    # input_file_path = parameters.get('input_file')
    input_file_path = "DTextD.mp4"
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
        video = VideoFileClip(outputFilePath)
        imageCv= cv2.imread(imageFilePath)
        image = ImageClip(imageCv)

        video_duration = video.duration

        start_sec = 2  # Start time in seconds
        end_sec = 6

        if start_sec < 0 or start_sec >= video_duration:
            raise ValueError("Start time must be between 0 and the video duration")
        if end_sec <= start_sec or end_sec > video_duration:
            raise ValueError("End time must be after the start time and within the video length")

        background_clip = video.subclip(t_start=0, t_end=video_duration)

        # Set image clip duration to match the image display time
        image_clip = image.set_duration(end_sec - start_sec)

        image_clip = image_clip.resize(newsize=background_clip.size)

        final_clip = CompositeVideoClip([background_clip, image_clip.set_start(start_sec)])

        # Write the final clip to the output video file
        final_clip.write_videofile(outputFilePath + f"_no_text.{extension}")

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
        return Result.getFailedResult("Unexpected error:" + str(e))
