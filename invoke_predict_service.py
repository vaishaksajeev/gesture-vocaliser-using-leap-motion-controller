"""
Class to invoke update_service
"""
from __future__ import print_function
from predict_service import PredictService
import numpy as np
import cv2
from autocorrect import autoCorrect
import pyttsx

def startPredict():
    predict_service = PredictService()
    #win=np.zeros([320,640,3],np.uint8)
    z=""
    try:
        while True:
            predict_service.capture_gesture()
            label = predict_service.predict_label()
            print (label, end='')
            z+=label
            win=np.zeros([320,640,3],np.uint8)
            cv2.namedWindow('image')
            img=cv2.putText(win, z, (4, 50), cv2.FONT_HERSHEY_TRIPLEX, 2, (255,255,255))
            cv2.imshow('image',win)
            k=cv2.waitKey(2000)
    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        x=autoCorrect(z)
        print (x)
        win=np.zeros([320,640,3],np.uint8)
        cv2.namedWindow('image')
        img=cv2.putText(win, x.upper(), (4, 50), cv2.FONT_HERSHEY_TRIPLEX, 2, (255,255,255))
        cv2.imshow('image',win)
        vocalizer=pyttsx.init()
        vocalizer.say(x)#replaced z with x
        vocalizer.runAndWait()
        prompt=raw_input("Do you want to input another word?y/n: ")
        if prompt=="y":
            cv2.destroyAllWindows()
            startPredict()
        cv2.destroyAllWindows()



