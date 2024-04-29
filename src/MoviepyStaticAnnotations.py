import cv2
from src.collager.util.api import Api



@Api(httpMethod="post")
def testing(parameters):
    video_path = '/Users/danialaslam/Documents/trillo-python-tutorial/src/text.mp4'
    output_path = '/Users/danialaslam/Documents/trillo-python-tutorial/src/Moviepystaticannotation.mp4'
    # Load the video

    cap = cv2.VideoCapture(video_path)
    # Get the video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    start_x, start_y = 100, 200
    end_x, end_y = 300, 400
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Define the codec and create VideoWriter object

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    # Loop through each frame
    while cap.isOpened():

        ret, frame = cap.read()
        if not ret:
            break

        # Draw annotations based on mouse input

        cv2.rectangle(frame, (start_x+300, start_y+300), (end_x+300, end_y+300), (0, 0, 0), thickness=-1)
        cv2.arrowedLine(frame, (start_x+225, start_y), (end_x+225, end_y), (0, 0, 0), thickness=25)
        cv2.circle(frame, (start_x+50, start_y+100), 100, (0, 0, 0), thickness=10)
        cv2.putText(frame, 'TEXT ON VIDEO', (150, 150), font, 4, (0, 25, 125), 15, cv2.LINE_4)
        cv2.imshow('Annotated Video', frame)
        # Write the annotated frame
        out.write(frame)


    # Release everything when done
    cap.release()
    out.release()
    cv2.destroyAllWindows()
