import cv2
from src.collager.util.api import Api

# Get the video properties
drawing = False
start_x, start_y = -1, -1
end_x, end_y = -1, -1
paused = False


@Api(httpMethod="post")
def testing(parameters):
    video_path = '/Users/danialaslam/Documents/trillo-python-tutorial/src/text.mp4'
    output_path = '/Users/danialaslam/Documents/trillo-python-tutorial/src/annotated_video.mp4'

    # Load the video
    # drawing = False
    # start_x, start_y = -1, -1
    # end_x, end_y = -1, -1

    # Mouse event callback function
    def draw_annotation(event, x, y, flags, param):
        global drawing, start_x, start_y, end_x, end_y

        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            start_x, start_y = x, y

        elif event == cv2.EVENT_MOUSEMOVE:
            if drawing:
                end_x, end_y = x, y

        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            end_x, end_y = x, y

    def toggle_pause():
        global paused
        paused = not paused

    # Load the video

    cap = cv2.VideoCapture(video_path)
    # Get the video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Define the codec and create VideoWriter object

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    # Create a window and set the mouse callback function
    cv2.namedWindow('Annotated Video')
    cv2.setMouseCallback('Annotated Video', draw_annotation)
    font = cv2.FONT_HERSHEY_SIMPLEX
    # Loop through each frame
    while cap.isOpened():

        ret, frame = cap.read()
        if not ret:
            break

        # Draw annotations based on mouse input
        if drawing:
            cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (0, 0, 0), thickness=-1)
            # cv2.arrowedLine(frame, (start_x, start_y), (end_x, end_y), (0, 0, 0), thickness=50)
            # cv2.circle(frame, (start_x, start_y), 100, (0, 0, 0), thickness=10)

            # cv2.addText(frame, "VIDEO EDITOR OPENCV", (start_x, start_y), "Arial", 1, (0, 0, 255), 2)
            #cv2.putText(frame, 'TEXT ON VIDEO', (150, 150), font, 4, (0, 25, 125), 15, cv2.LINE_4)

        # Write the annotated frame
        out.write(frame)
        if not paused:
            cv2.imshow('Annotated Video', frame)

        else:
            pause_text = "Paused - Press any key to resume"
            cv2.putText(frame, pause_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Annotated Video', frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('p'):
            toggle_pause()

    # Release everything when done
    cap.release()
    out.release()
    cv2.destroyAllWindows()
