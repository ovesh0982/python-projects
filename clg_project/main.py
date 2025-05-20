import cv2
import numpy as np

# Open the video file
video = cv2.VideoCapture("C:/Users/DESKTOP/Desktop/python/clg_project/green.mp4")

# Read the background image
image = cv2.imread("C:/Users/DESKTOP/Desktop/python/clg_project/bg.jpg")

# Ensure the background image and video frames are the same size
# We'll resize the background image to match the video frame size
while True:
    ret, frame = video.read()

    if not ret:
        break  # Break the loop if we can't read a frame (end of video)

    # Resize frame to 640x480
    frame = cv2.resize(frame, (640, 480))

    # Resize background image to match the frame size
    image_resized = cv2.resize(image, (640, 480))

    # Define the color range for green color (in HSV)
    u_green = np.array([104, 153, 70])
    l_green = np.array([30, 30, 0])

    # Mask the green area in the video frame
    mask = cv2.inRange(frame, l_green, u_green)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Subtract the green area from the frame to get the remaining part of the image
    f = frame - res

    # Replace the green area with the background image
    f = np.where(f == 0, image_resized, f)

    # Display the original frame and the processed frame
    cv2.imshow("video", frame)
    cv2.imshow("mask", f)

    # Exit the loop if the ESC key is pressed
    if cv2.waitKey(25) == 27:
        break

# Release the video capture object and close all OpenCV windows
video.release()
cv2.destroyAllWindows()
