# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 14:50:54 2018

@author: khushboo
"""

import os
import cv2
import numpy as np
from PIL import Image

#recogniser = cv2.createLBPHFaceRecognizer()
recogniser = cv2.face.LBPHFaceRecognizer_create()
path = 'DataSets'


def getImagesWithID(path):
    #creating list of all images in directory datasets
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faces = []
    IDs = []
    
    for imgPath in imagePaths:
        # this is pil image and converting to gray scale
        faceImg = Image.open(imgPath).convert('L')
        #convert pil image to numpy array
        faceNp = np.array(faceImg,'uint8')
        #getting id from image
        ID = int(os.path.split(imgPath)[-1].split('_')[0])
        #extract the face from training image sample
        faces.append(faceNp)
        IDs.append(ID)
        cv2.imshow('training',faceNp)
        cv2.waitKey(10)
    return np.array(IDs), faces

IDs,faces = getImagesWithID(path)
recogniser.train(faces,IDs)
recogniser.save('recogniser/trainingData.yml')
#recogniser.write('recogniser/trainingData.yml')
cv2.destroyAllWindows()
