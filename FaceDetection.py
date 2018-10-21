import cv2, time
video = cv2.VideoCapture(0)
# check, frame = video.read()
# frame checks if the process executes well!
# print(check)
# print(frame)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# time.sleep(3)
while True:
    check, frame = video.read()
#     print(check)
#     print(frame)
#     if frame == True:
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    print(gray)
    faces = face_cascade.detectMultiScale(gray
                                      ,scaleFactor=1.4
                                      ,minNeighbors=5)
    print(faces)
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow("Capturing",frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
# cv2.imshow("Capturing",frame)
# cv2.waitKey(0)
video.release()
cv2.destroyAllWindows()
# video.release()
# sleep allows you to engage the camera for 3 seconds