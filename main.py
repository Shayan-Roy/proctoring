import cv2
face_cascade=cv2.CascadeClassifier("C:/Users/User/Desktop/haarcascade_frontalface_default.xml")
webcam=cv2.VideoCapture(0)
while True:
    success,img= webcam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,255,0),2)

    cv2.imshow("image",img)
    cv2.waitKey(1)


