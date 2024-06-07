# from moviepy.editor import VideoFileClip, ImageClip
# from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
#
# def add_image_to_video(video_path, image_path, start_sec, end_sec, output_path):
#
#     # Load video and image clips
#     video = VideoFileClip(video_path)
#     image = ImageClip(image_path)
#
#     # Get video duration
#     video_duration = video.duration
#
#     # Ensure valid time range
#     if start_sec < 0 or start_sec >= video_duration:
#         raise ValueError("Start time must be between 0 and the video duration")
#     if end_sec <= start_sec or end_sec > video_duration:
#         raise ValueError("End time must be after the start time and within the video length")
#
#     # Clip the video for the desired portion excluding the image
#     video_clip_without_image = video.subclip(t_start=0, t_end=start_sec).set_duration(
#         video_duration - (end_sec - start_sec))
#
#     # Set image clip duration to match the image display time
#     image_clip = image.set_duration(end_sec - start_sec)
#
#     # Resize the image to match the video frame size (optional)
#     if image.size != video.size:
#         image_clip = image_clip.resize(width=video.w, height=video.h)
#
#     # Create a composite clip with video and image (adjust position as needed)
#     final_clip = CompositeVideoClip([video_clip_without_image, image_clip.set_pos('center')])
#
#     # Write the final clip to the output video file
#     final_clip.write_videofile(output_path)
#
#     print("Video processing complete!")
#
#
# # Example usage
# video_path = "/Users/danialaslam/Documents/trillo-python-tutorial/src/Data/text.mp4"
# image_path = "/Users/danialaslam/Documents/trillo-python-tutorial/src/Data/imagetobeadded.png"
# start_sec = 2  # Start time in seconds
# end_sec = 8  # End time in seconds
# output_path = "/Users/danialaslam/Documents/trillo-python-tutorial/src/Data/output_video.mp4"
# add_image_to_video(video_path, image_path, start_sec, end_sec, output_path)



#

from moviepy.editor import VideoFileClip, ImageClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip

from src.collager.util import LogApi


def add_image_to_video(video_path, image_path, start_sec, end_sec, output_path):

    # Load video and image clips
    video = VideoFileClip(video_path)
    image = ImageClip(image_path)

    # Get video duration
    video_duration = video.duration

    # Ensure valid time range
    if start_sec < 0 or start_sec >= video_duration:
        raise ValueError("Start time must be between 0 and the video duration")
    if end_sec <= start_sec or end_sec > video_duration:
        raise ValueError("End time must be after the start time and within the video length")

    # Create a clip with original video duration (assuming constant FPS)
    background_clip = video.subclip(t_start=0, t_end=video_duration)

    # Set image clip duration to match the image display time
    image_clip = image.set_duration(end_sec - start_sec)

    # Resize image with aspect ratio preservation

    LogApi.auditLogInfo("Original Image size: " + str(image.w))
    LogApi.auditLogInfo("Original Image height: " + str(image.h))
    LogApi.auditLogInfo("Video size: " + str(video.w))
    LogApi.auditLogInfo("Video height: " + str(video.h))
    LogApi.auditLogInfo("background_clip size: " + str(background_clip.w))
    LogApi.auditLogInfo("background_clip height: " + str(background_clip.h))

    image_clip = image_clip.resize(newsize=background_clip.size)
    # size = clip.size


    LogApi.auditLogInfo("Resized Image size: " + str(image_clip.w))
    LogApi.auditLogInfo("Resized Image height: " + str(image_clip.h))
    # Create a composite clip with video and image (adjust position as needed)
    final_clip = CompositeVideoClip([background_clip, image_clip.set_start(start_sec)])

    # Write the final clip to the output video file
    final_clip.write_videofile(output_path)

    print("Video processing complete!")

# Example usage (assuming paths are correct)
video_path = "/Users/danialaslam/Documents/trillo-python-tutorial/src/Data/text.mp4"
image_path = "/Users/danialaslam/Documents/trillo-python-tutorial/src/Data/image.png"
start_sec = 2  # Start time in seconds
end_sec = 6  # End time in seconds
output_path = "/Users/danialaslam/Documents/trillo-python-tutorial/src/Data/output_video.mp4"
add_image_to_video(video_path, image_path, start_sec, end_sec, output_path)
