import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

cap = cv2.VideoCapture(0)
while True:

     _,img = cap.read()
     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

     faces = face_cascade.detectMultiScale(gray,1.3,5)

     for (x,y,w,h) in faces:
         cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)

     cv2.imshow('img',img)
     k = cv2.waitKey(30) & 0xFF== ord('q')
     if k == 27:
         break
cap.release()
cv2.destroyAllWindows()