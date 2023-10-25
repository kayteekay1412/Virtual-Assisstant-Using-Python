# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21

@author: ktk
"""
import wikipedia,smtplib,random,webbrowser,math,requests 
from pytube import YouTube
from bs4 import BeautifulSoup
from googletrans import Translator,constants
from Functions import speak,sub,hear
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
affirm=["yes","y","Y","Yes","YES"]

def otp():
    speak("Enter your email id to receive your OTP.")
    to=input("Enter your e-mail address: ")
    digits="0123456789"
    otp=""
    me="myemail@gmail.com"
    for i in range(4):
        otp+=digits[math.floor(random.random()*10)]
    speak("You should be getting an OTP on your email id.")
    text=f"Hey User,\nI hope you enjoy using ktk.\nYour OTP to activate ktk is: {otp}"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(me, 'password')
    server.sendmail(me, to, text)
    server.close()
    count=3
    while True:
        speak("Enter your OTP to proceed.")
        otpp=(input("Enter the OTP: "))
        if otpp==otp:
            speak("You have activated 'ktk' succesfully.")
            break
        else:
            speak("Error!! You have entered the wrong OTP. Please try again.")
            count=count-1
            if count>0:
                continue
            else:
                speak("You have been unsuccesful. Try again.")
                break
def wikisearch():
    speak("What do you want to search on wikipedia?")
    query=input("Enter your query below:\n")
    # while True:
    #     try:
    #         com=hear()
    #         break
    #     except:
    #         speak("Sorry I didn't catch that")
    # query=com.lower()
    speak('Searching Wikipedia...')
    try:
        results = wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        sub(results)
    except:
        speak(f"Sorry. I couldn't find anything on {query} on wikipedia")
def wikirandom():
    while True:
        webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))        
        speak("Lemme reccomend a random article")
        a="https://en.wikipedia.org/wiki/Special:Random"
        u=requests.get(a)
        soup=BeautifulSoup(u.content,'html.parser')
        title=soup.find(class_="firstHeading").text
        print(title)
        speak("Do you want to read this article?")
        ans=input("Do you want to view this article?")
        if ans in affirm:
            url="https:\\en.wikipedia.org\wiki\%s"
            webbrowser.get('chrome').open(url)            
            break
        else:
            sub("OK. ktk will search for another inetresting article.")
            continue      
def gsearch():
    webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
    speak("What do you want to know?")
    site=input("Enter your query: ")
    site=site.split()
    speak(f"Asking Google about {site} now")
    link="www.google.com/search?q="
    for i in site:
        link=link+"+"+i
    webbrowser.get('chrome').open(link)
def sendmail():
    me="myemail@gmail.com"
    speak("Who should I send the email to? ")
    to=input("Who should I send the email to? ")
    speak("What should I send in the email? ")
    content=input("What should I send in the email? \n")
    speak("Sending mail now...")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(me, 'password')
    server.sendmail(me, to, content)
    speak("E-mail has been sent sucessfully.")
    server.close()
def insta():
    webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
    speak("Opening Instagram now")
    webbrowser.get('chrome').open("instagram.com")
def opensite():
    webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
    speak("Which site do you want to open?")
    site=input("Enter the name of the site: ")
    speak(f"Opening {site} now")
    link=site+".com"
    webbrowser.get('chrome').open(link)
def translatetext():
    c=(input("Do you want to\n1)translate text to English?\n2)translate to another language? "))
    tr=Translator()
    if c=="1":
        speak("What do you want to translate")
        text=input("Enter the text to be translated: ")
        a=tr.translate(text)
        sub(f"{text} has been translated to English as: {a.text}")
    elif c=="2":
        speak("What do you want to translate")
        text=input("Enter the text to be translated: ")
        speak("Which language do you want to translate to?")
        l=constants.LANGUAGES
        count=1
        for i in l:
            print(count,")","Langauge: ",l[i]," ||","Code: ",i)
            count=count+1
        code=input("Enter code for the language you want to translate it to: ")
        a=tr.translate(text,dest=code)
        sub(f"{text} has been translated from English as: {a.text}")
def youtube():
    speak("Do you want to download a single video or multiple videos?")
    n=int(input("1)Single Videos\n2)Multiple Videos "))
    if n==1:
        link=input("Paste the link here: ")
        yt = YouTube(link)  
        speak("Enter file name below")
        n=input("Save video as: ")
        try:
            yt.streams.filter(progressive = True, file_extension = "mp4").first().download(output_path = "D:\\ktk\\Downloads", filename=n)
            sub("The video has been downloaded succesfully.")
        except:
            sub("An error has occured.")
    elif n==2:
        speak("How many videos are there?")
        nn=int(input("how many videos are there? "))
        for i in range(nn):
            speak(f"Enter the link for the {ordinal(i+1)} video below ")
            link=input("Paste the link here: ")
            yt = YouTube(link)  
            speak("Enter file name")
            n=input("Save video as: ")
            try:
                yt.streams.filter(progressive = True, file_extension = "mp4").first().download(output_path = "D:\\ktk\\Downloads", filename=n)
                sub("The video has been downloaded succesfully.")
            except:
                sub("An error has occured.")
