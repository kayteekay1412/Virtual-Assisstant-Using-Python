# -*- coding: utf-8 -*-
"""
Created on Tue Jun 1

@author: ktk
"""

import subprocess,wolframalpha,pyttsx3,tkinter,json,random,operator,datetime,wikipedia,webbrowser,os,winshell,feedparser,ctypes,smtplib,time,requests,shutil
import speech_recognition as sr
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from Functions import sub
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 0.7
        audio = r.listen(source)
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
    return query
def usrname():
    speak("what shall I call you?")
    uname=takeCommand()
    speak("Welcome Master")
    speak(uname)
    columns=shutil.get_terminal_size().columns    
    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
    speak("How can I help you, Sir")
if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    takeCommand()     
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            sub(results)
        elif 'open YouTube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")  
        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            music_dir = "C:\\Users\\ktk\\Music"
            songs = os.listdir(music_dir)
            print(songs)   
            random = os.startfile(os.path.join(music_dir, songs[1]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")   
            speak(f"Sir, the time is {strTime}")
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query
        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")
        elif "what's your name" in query or "What is your name" in query:
            sub("My friends call me", assname)
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by ktk.") 
        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)
        elif "who i am" in query:
            speak("If you talk then definately your human.")
        elif "why you came to world" in query:
            speak("Thanks to ktk. If you want further information, I'm sorry that's a secret.")
        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
        elif "who are you" in query:
            speak("I am your virtual assistant created by ktk")
        elif 'reason for you' in query:
            speak("I was created as a project by krk ")
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed succesfully")
        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop JARVIS from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))
        elif "update assistant" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream = True)
            with open("Voice.py", "wb") as Pypdf:
                total_length = int(r.headers.get('content-length'))
                for ch in progress.bar(r.iter_content(chunk_size = 2391975),
                                       expected_size =(total_length / 1024) + 1):
                    if ch:
                      Pypdf.write(ch)
        elif "jarvis" in query:
            speak("Jarvis 1 point o in your service Mister")
            speak(assname)
        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")
        elif "Good Morning" in query:
            speak("A warm" +query)
            speak("How are you Mister")
            speak(assname)
        elif "will you be my gf" in query or "will you be my bf" in query:  
            speak("I'm not sure about, may be you should give me some time")
        elif "how are you" in query:
            speak("I'm fine, glad you me that")
        elif "i love you" in query:
            speak("It's hard to understand")
        elif "what is" in query or "who is" in query:
            client = wolframalpha.Client("API_ID")
            res = client.query(query)
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")