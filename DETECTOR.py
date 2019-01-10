# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 20:07:23 2018

@author: khushboo
"""

import cv2
import sqlite3


faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#to capture image
cam = cv2.VideoCapture(0)
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read('recogniser/trainingData.yml')
id = 0
#font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,5)
font = cv2.FONT_HERSHEY_SIMPLEX


while(True):
    #it return one status variable and captured image
    ret,image = cam.read() 
    #color img to grayscale img
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces  = faceDetect.detectMultiScale(gray,1.3,5)
    connection = sqlite3.connect("Face_database.db")
    att = 'P'

    for(x,y,w,h) in faces:
        name= ' '
        cv2.rectangle(image,(x,y),(x+w,y+h),(200,0,0),1)
        id,conf = rec.predict(gray[y:y+h,x:x+w])
        print(id)
        
        if(id==1):
            name = 'Khushboo'
            cmd = "UPDATE Student SET ATTENDANCE='"+str(att)+"' WHERE ID="+str(id)
            cursor = connection.execute(cmd)
            break
        elif(id==2):
            name='Nitish'
            cmd = "UPDATE Student SET ATTENDANCE='"+str(att)+"' WHERE ID="+str(id)
            cursor = connection.execute(cmd)  
            break
        elif(id==3):
            name='Ayush'
            cmd = "UPDATE Student SET ATTENDANCE='"+str(att)+"' WHERE ID="+str(id)
            cursor = connection.execute(cmd)   
            break
        elif(id==4):
            name='Sahil'
            cmd = "UPDATE Student SET ATTENDANCE='"+str(att)+"' WHERE ID="+str(id)
            cursor = connection.execute(cmd) 
            break
        elif(id==5):
            name='Akansha'
            cmd = "UPDATE Student SET ATTENDANCE='"+str(att)+"' WHERE ID="+str(id)
            cursor = connection.execute(cmd) 
            break
        elif(id==6):
            name='Ankit'
            cmd = "UPDATE Student SET ATTENDANCE='"+str(att)+"' WHERE ID="+str(id)
            cursor = connection.execute(cmd) 
            break       
        elif(id==7):
            name='Ashraf'
            cmd = "UPDATE Student SET ATTENDANCE='"+str(att)+"' WHERE ID="+str(id)
            cursor = connection.execute(cmd) 
            break
        elif(id==8):
            name='Ruchika'
            cmd = "UPDATE Student SET ATTENDANCE='"+str(att)+"' WHERE ID="+str(id)
            cursor = connection.execute(cmd) 
            break      
        elif(id==9):
            name='Monica'
            cmd = "UPDATE Student SET ATTENDANCE='"+str(att)+"' WHERE ID="+str(id)
            cursor = connection.execute(cmd) 
            break
        elif(id==15):
            name='Zameer Khan'
            cmd = "UPDATE Student SET ATTENDANCE='"+str(att)+"' WHERE ID="+str(id)
            cursor = connection.execute(cmd) 
            break
        elif(id==10):
            name=''
            cmd = "UPDATE Student SET ATTENDANCE='"+str(att)+"' WHERE ID="+str(id)
            cursor = connection.execute(cmd) 
            break
        elif(id==11):
            name=''
            cmd = "UPDATE Student SET ATTENDANCE='"+str(att)+"' WHERE ID="+str(id)
            cursor = connection.execute(cmd) 
            break
            
    cv2.putText(image,name,(x,y-10),font,0.55,(0,0,0),1)      
    connection.commit()
    connection.close()
    
    cv2.imshow('face',image)
    if(cv2.waitKey(1) == ord('q')):
        break

cam.release()
cv2.destroyAllWindows()

