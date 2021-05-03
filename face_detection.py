import cv2

# Reading the cascade frontal face data
face_cascade = cv2.CascadeClassifier(r"C:\Users\prave\Desktop\V.3.0\Projects\DS Projects\Youtube\haarcascade_frontalface_default.xml")

# Using the webcam capturing the frames for face detection purpose
capture_video_from_webcam = cv2.VideoCapture(0)

# Infinite loop to loop thorough each frame in the video
while True:

    # This reads each frame from the video
    _,image = capture_video_from_webcam.read()
    # Convertion of colored images to gray scale
    gray_scale_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # DetectMultiScale function is used to detect the faces, we are giving 3 arguments input: image, scaleFactor and minNeighbours.
    face = face_cascade.detectMultiScale(gray_scale_image,1.1,4)
    # Looping to draw a rectangle
    for (x, y, w, h) in face:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # Display
        cv2.imshow("image", image)
        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break


capture_video_from_webcam.release()

