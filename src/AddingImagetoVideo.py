import cv2

from src.collager.util import LogApi
from src.collager.util.api import Api


# Load the video


def testing(parameters):
    video_path = "/Users/danialaslam/Documents/trillo-python-tutorial/src/text.mp4"
    cap = cv2.VideoCapture(video_path)

    # Get the video properties
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    LogApi.logInfo(frame_width)
    LogApi.logInfo(frame_height)

    # Desired timestamp to add the image (in seconds)
    start_timestamp = 7
    end_timestamp = 9
    output_path = "/Users/danialaslam/Documents/trillo-python-tutorial/src/imageadded.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))
    check = True

    # Read frames until the desired timestamp
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Get the current timestamp
        current_timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0

        # Check if we've reached the desired timestamp
        if start_timestamp <= current_timestamp <= end_timestamp:
            # Load the image to add
            image_path = "/Users/danialaslam/Documents/trillo-python-tutorial/src/imagetobeadded.png"
            image_with_alpha = cv2.imread(image_path)

            if image_with_alpha.shape[2] == 4:
                image = cv2.cvtColor(image_with_alpha, cv2.COLOR_BGRA2BGR)
            else:
                image = image_with_alpha

            # Resize the image to fit the frame
            image_height, image_width = image.shape[:2]
            image = cv2.resize(image, (frame_width, frame_height))
            image_height, image_width = image.shape[:2]
            LogApi.logInfo(image_width)
            LogApi.logInfo(image_height)

            LogApi.logInfo(image.shape[0])
            LogApi.logInfo(image.shape[1])

            if image_height == frame_height and image_width == frame_width:
                print("Image resized successfully.")
            else:
                print("Failed to resize the image to match the frame dimensions.")

            # Overlay the image onto the frame
            # You can adjust the position of the image as per your requirements
            x_offset = 0  # adjust the x offset
            y_offset = 0  # adjust the y offset
            frame[y_offset:y_offset + image.shape[0], x_offset:x_offset + image.shape[1]] = image
            out.write(frame)
            # check = False
            # continue

        out.write(frame)

    # Define the codec and create VideoWriter object
    # output_path = "/Users/danialaslam/Documents/trillo-python-tutorial/src/imageadded.mp4"
    # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    # out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    # Write the frame with the overlaid image to the output video
    # out.write(frame)

    # Release everything when done
    cap.release()
    out.release()
    cv2.destroyAllWindows()


