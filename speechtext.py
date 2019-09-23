"""
please install Pyaudio and speechrecognition

open cmd and install the following commands

pip install SpeechRecognition

pip install pyaudio

use python 3.6 or earlier.

Python 3.7 is not supported by Pyaudio library.

"""

import cv2
import speech_recognition as sr
def reverse():
        r = sr.Recognizer()

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source ,duration=3)
            print('say something!!!')
            audio = r.listen(source)
            print('Done!')
            
        
        try:
            text = r.recognize_google(audio, language= 'en-IN')
            print ('you said: ' + text)
            cv2.namedWindow('image')
            trn = cv2.imread('transition.jpg',-1)
            for i in text:
                if ord(i)!=32:
                        i+=".jpg"
                        img = cv2.imread(i,-1)
                        cv2.imshow('image',img)
                        cv2.waitKey(2000)
                        cv2.imshow('image',trn)
                        cv2.waitKey(1000)
                else:
                        i+=".jpg"
                        cv2.imshow('image',trn)
                        cv2.waitKey(1000)
            cv2.destroyWindow('image')
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        


