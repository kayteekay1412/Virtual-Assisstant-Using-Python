# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30

@author: ktk
"""

# imp functions
import pyttsx3,wikipedia,smtplib,os,random,webbrowser,math,requests,os
import speech_recognition as sr
from bs4 import BeautifulSoup
def speak(audio):
    engine.say(audio)
    engine.runAndWait()    
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def sub(x):
    print(x)
    speak(x)
def hear():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.7
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language ='en')
    except Exception as e:
        print(e)   
        sub("Unable to Recognize your voice.") 
        return "None"
    return query
def clear():
    os.system('cls')
    
# r=sr.Recognizer()
# with sr.Microphone() as source:
#     r.adjust_for_ambient_noise(source)
#     r.pause_threshold = 0.7
#     audio = r.listen(source)
#     try:
#         query = r.recognize_google(audio, language ='en')
#         print(query)
#     except Exception as e:
#         print(e)   
#         sub("Unable to Recognize your voice.") 
    