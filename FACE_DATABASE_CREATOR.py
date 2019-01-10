# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 14:15:45 2018

@author: khushboo
"""

#  FACE DETECTION
''' create the dataset
    train the recognizer
    detector'''
    
    

import cv2
import sqlite3

#to capture image
cam = cv2.VideoCapture(0)
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def insertOrUpdate(Id,Name,Branch):
    connection = sqlite3.connect('Face_database.db')
    #execute the command which will check id is present in database or not
    cmd = 'SELECT * FROM Student Where ID='+str(Id)
    #execute command returns a cursor
    #cursor return row by row detsils
    cursor = connection.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if(isRecordExist == 1):
        cmd = "UPDATE Student SET NAME='"+str(Name)+"',BRANCH ='"+str(Branch)+"' WHERE ID="+str(Id)
    else:
        cmd = "INSERT INTO Student(ID,NAME,BRANCH) VALUES('"+str(Id)+"','"+str(Name)+"','"+str(Branch)+"')"
    connection.execute(cmd)
    connection.commit()
    connection.close()

id = int(input('Enter user ID :'))
name = input('Enter Name :')
branch = input('Enter the branch name :')
insertOrUpdate(id,name,branch)

sampleNum = 0

while(True):
    #it return one status variable and captured image
    ret,image = cam.read() 
    #color img to grayscale img
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces  = faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        sampleNum += 1 
        cv2.imwrite('DataSets/'+str(id)+'_'+str(sampleNum)+'.jpg',gray[y:y+h,x:x+w])
        cv2.rectangle(image,(x,y),(x+w,y+h),(200,0,0),1)
        cv2.waitKey(100)
        
    cv2.imshow('face',image)
    if(sampleNum>99):
        break

cam.release()
cv2.destroyAllWindows()


