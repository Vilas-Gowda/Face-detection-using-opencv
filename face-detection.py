import cv2
import os


inpt1= 0 
while(inpt1 != 1 and inpt1 != 2):
    inpt1 = int(input("Detect Faces in 1.Picture 2.Videos  - "))


if(inpt1 == 1):

    path = input("enter Image path - ")

    img = cv2.imread(path)

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.09, 4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x, y), (x+w, y+h),(255,0,0),2)

    cv2.imshow('img', img)
    cv2.waitKey() 
elif(inpt1 == 2):

    path = input("enter video path - ")

    cap = cv2.VideoCapture(path)

    while True:
        _, img = cap.read()
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.09, 4)

        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x, y), (x+w, y+h),(255,0,0),2)

        cv2.imshow('img', img)

        k = cv2.waitKey(30) & 0xff
        if( k ==27):
            break
