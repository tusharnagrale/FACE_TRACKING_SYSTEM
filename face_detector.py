""""problem: create a system for face tracking system inside a webcam video

working:
1. open video stream using python library
2. ask user to draw bounding box on the window using mouse click 
3. initialize face detector
4. if face box lies within the user defined box then initialize the tracker for the face."""""
#date:june 24 2020


import cv2
#classifier to detect face
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#creating video object
cam_capture = cv2.VideoCapture(0)

#to destroy all windows
cv2.destroyAllWindows()

while True:
    _, img = cam_capture.read()

    showCrosshair = False

    # drag a rectangle from the top left corner to the bottom right corner
    # instead of the dragging it from the center
    fromCenter = False

    # selectROI function allows user to select the particular area of image for processing or image manipulation
    r = cv2.selectROI("select the region of interest and press (space/enter) to continue", img, fromCenter, showCrosshair)

    break

while True:
    _, image_frame = cam_capture.read()

    #the selected region will be only send for face detection
    rect_img = image_frame[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]

    #conversion of image to gray
    gray = cv2.cvtColor(rect_img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each facent
    for (x, y, w, h) in faces:
        cv2.rectangle(rect_img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    #for displaying live image
    cv2.imshow("face_detection live cam in selected region", image_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam_capture.release()
cv2.destroyAllWindows()