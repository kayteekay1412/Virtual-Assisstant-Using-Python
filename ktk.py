"""
RA2111053010055 - Karthikeyan Nandakumar
@author: ktk
"""
# THIS IS IT
import webbrowser, itertools
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier,SGDClassifier
from sklearn.metrics import accuracy_score, confusion_matrix,classification_report
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
import TimeOfTheDay as t
import Games as gg
import IPaddress as ip
import Conversions as convert
import Calculator as c
import Crypto as crypt
import FunFacts as fun
import Internet as net
import Functions as func
import General as gen
from Functions import sub,speak
used=1
u=0
while True:
    k=input("[TAP A KEY TO ACTIVATE] ")
    if k=="0":
        sub(t.goodbye(name="User"))
        sub("Thank you for using ktk!")
        break
    else:
        if used==0:
            net.otp()
        u+=1
        if u==1:    
            sub("Before we begin, may I know your name?")
            name=input("Enter your name here: ")
            func.speak(t.chronos(name))
        func.speak("How can I help you?")
        comms=input("Enter command below:\n")
        comms=comms.lower()
        print()
        if 'wikipedia' in comms:
            net.wikisearch()
        elif "google" in comms:
            net.gsearch()
        elif "what is the time" in comms:
            t.now()
        elif "ip address" in comms:
            sub(ip.ipaddress())
        elif "stopwatch" in comms:
            t.stopwatch()
        elif "timer" in comms:
            t.timer()
        elif "random" and "wikipedia" in comms:
            net.wikirandom()
        elif "email" in comms:
            net.sendmail()
        elif "insta" in comms:
            net.insta()
        elif "open site" in comms:
            net.opensite()
        elif "translate" in comms:
             net.translatetext()
        elif "youtube" and "download" in comms:
            net.youtube()
        elif "music" in comms:
            gen.music()
        elif "sort" and "words" in comms:
            gen.sortwords()
        elif "grocery" in comms:
            gen.grocerylist()
        elif "calender" in comms:
            gen.calender()
        elif "reminder" in comms:
            gen.desktopreminder()
        elif "games" in comms:
            library={1:"Magic Ball",2:"Dice",3:"Rock Paper Scissors or Janken",4:"Tic Tac Toe",5:"Survival Game",6:"Hangman",7:"Guess The Number",8:"2048",9:"Guess The Animal",10:"Spin A Yarn",11:"Guess The Quote",12:"Draw Cards",13:"Give Cards",14:"Guess the Card",15:"Text-based Adventure"}
            speak("Which game do you want to play?")
            for i in library:
                print(f"{i}) {library[i]}")
            n=int(input("Enter the number of the game: "))
            sub(f"You have decided to play {library[n]}.")
            if n==1:
                gg.magicball()
            elif n==2:
                gg.dice()
            elif n==3:
                gg.janken()
            elif n==4:
                gg.tictactoe()
            elif n==5:
                gg.survivalgame()
            elif n==6:
                gg.hangman()
            elif n==7:
                gg.guessthenumber()
            elif n==8:
                gg.game2048()
            elif n==9:
                gg.guesstheanimal()
            elif n==10:
                gg.spinayarn()
            elif n==11:
                gg.guessthequote()
            elif n==12:
                gg.drawcards()
            elif n==13:
                gg.givecards()
            elif n==14:
                gg.guessthenumber()
            elif n==15:
                gg.textadventure()
        elif "fun facts" in comms:
            fun.funfact()
        elif "open youtube" in comms:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
        elif 'open google' in comms:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")
        elif 'how are you' in comms:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
        elif 'fine' in comms or "good" in comms:
            speak("It's good to know that your fine")
        elif 'exit' in comms:
            speak("Thanks for giving me your time")
            exit()
        elif "who i am" in comms:
            speak("If you talk then definately your human.")
        elif "why you came to world" in comms:
            speak("Thanks to ktk. If you want further information, I'm sorry that's a secret.")
        elif 'is love' in comms:
            speak("It is 7th sense that destroy all other senses")
        elif "who are you" in comms:
            speak("I am your virtual assistant created by ktk")
        elif 'reason for you' in comms:
            speak("I was created as a project by ktk")
        elif "Good Morning" in comms:
            speak("A very warm morning!")
            speak(f"How are you Mister {name}")
        elif "how are you" in comms:
            speak("I'm fine, glad you me that")
        elif "i love you" in comms:
            speak("It's hard to understand")
        elif "encrypt caesar" in comms or "caesar" in comms:
            crypt.casearcode()
        elif "encrypt morse" in comms or "morse" in comms:
            crypt.morsecode()
        elif "encrypt vigenre" in comms or "vigenre" in comms:
            crypt.vigenre()
        elif "convert" in comms:
            speak("Welcome to smart converter")
            sub("which conversion do you want to perform?")
            print("1. Temperature\n2. Programming Units\n3.Speed\n4. Units")
            n=int(input("Enter option here:"))
            if n==1:
                convert.temp()
            if n==2:
                convert.programunits()
            if n==3:
                convert.speed()
            if n==4:
                convert.units()
        elif "math" in comms:
            speak("Welcome to smart calculator.")
            sub("What operation do you want to perform?")
            ops={1: 'Power', 2: 'Matrix', 3: 'Multiples', 4: 'Simple Calculation', 5: 'Factorization', 6: 'Factorial', 7: 'Simple Interest', 8: 'Compound Interest', 9: 'All Primes in a given range', 10: 'Fibonacci Sequence', 11: 'Quadratic Equation Solver', 12: 'Flyod Triangle', 13: 'Geometrical Calculations', 14: 'Leap Year or Not', 15: 'Days between two dates', 16: 'Days left in a month', 17: 'Pythagorean Theorem', 18: 'Trignometric Calculations', 19: 'Log calculations', 20: 'Greatest Commond Divisor', 21: 'Root of given number', 22: 'Prime Factorization', 23: 'To check Prime or Not', 24: 'To check if number is Palindromic or not', 25: 'To check if number is Armstrong or not', 26: 'To check if number is strong number or not', 27: 'To check if number is perfect number or not', 28: 'ASCII conversion', 29: 'Numbers that are not divisible', 30: 'Profit Loss Calculations', 31: 'Convert to Roman Numerals', 32: 'Calculate Student Grade'}
            for zz in ops:
                print(f"{zz}) {ops[zz]}")
            n=int(input("Enter your option here: "))
            if n==1:
            	c.power()
            if n==2:
            	c.matrix()
            if n==3:
            	c.multiples()
            if n==4:
            	c.calculate()
            if n==5:
            	c.factor()
            if n==6:
            	c.factorial()
            if n==7:
            	c.si()
            if n==8:
            	c.ci()
            if n==9:
            	c.allprime()
            if n==10:
            	c.fibonacci()
            if n==11:
            	c.quadratic()
            if n==12:
            	c.flyodtriangle()
            if n==13:
            	c.geometry()
            if n==14:
            	c.leapornot()
            if n==15:
            	c.daysbetween()
            if n==16:
            	c.daysleftinmonth()
            if n==17:
            	c.pythagorean()
            if n==18:
            	c.trigonometry()
            if n==19:
            	c.log()
            if n==20:
            	c.greatestcommondivisor()
            if n==21:
            	c.root()
            if n==22:
            	c.primefactors()
            if n==23:
            	c.isprime()
            if n==24:
            	c.ispalindrome()
            if n==25:
            	c.armstrong()
            if n==26:
            	c.strongnum()
            if n==27:
            	c.perfectnum()
            if n==28:
            	c.asciinum()
            if n==29:
            	c.numthatarenotdivisble()
            if n==30:
            	c.profitloss()
            if n==31:
            	c.romannumerals()
            if n==32:
            	c.studentgrade()
        elif "data analysis" in comms:
            sub("Welcome to Data Analysis Projects")
            print("1. Fake News Detector\n2. Wine Quality Detection")
            n=int(input("Enter your choice: "))
            if n==1:
                df=pd.read_csv(r'D:\Karthik\Python Programs\ktk\NEW\Data Analysis\Fake News Detector\news.csv')
                (df.shape)
                (df.head())
                labels=df.label
                (labels.head(100))
                x_train,x_test,y_train,y_test=train_test_split(df['text'], labels, test_size=0.2, random_state=7)
                tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7)
                tfidf_train=tfidf_vectorizer.fit_transform(x_train) 
                tfidf_test=tfidf_vectorizer.transform(x_test)
                pac=PassiveAggressiveClassifier(max_iter=50)
                (pac.fit(tfidf_train,y_train))
                y_pred=pac.predict(tfidf_test)
                score=accuracy_score(y_test,y_pred)
                print("Fake News Detector has been run on the given dataset.")
                print(f'Accuracy of the modal: {round(score*100,2)}%')
                (confusion_matrix(y_test,y_pred, labels=['FAKE','REAL']))
            if n==2:
                wine = pd.read_csv("D:/Karthik/Python Programs/ktk/NEW/Data Analysis/Wine Quality Detection/winequality-red.csv")
                fig = plt.figure(figsize = (10,6))
                sns.barplot(x = 'quality', y = 'fixed acidity', data = wine)
                fig = plt.figure(figsize = (10,6))
                sns.barplot(x = 'quality', y = 'volatile acidity', data = wine)
                fig = plt.figure(figsize = (10,6))
                sns.barplot(x = 'quality', y = 'citric acid', data = wine)
                fig = plt.figure(figsize = (10,6))
                sns.barplot(x = 'quality', y = 'residual sugar', data = wine)
                fig = plt.figure(figsize = (10,6))
                sns.barplot(x = 'quality', y = 'chlorides', data = wine)
                fig = plt.figure(figsize = (10,6))
                sns.barplot(x = 'quality', y = 'free sulfur dioxide', data = wine)
                fig = plt.figure(figsize = (10,6))
                sns.barplot(x = 'quality', y = 'total sulfur dioxide', data = wine)
                fig = plt.figure(figsize = (10,6))
                sns.barplot(x = 'quality', y = 'sulphates', data = wine)
                fig = plt.figure(figsize = (10,6))
                sns.barplot(x = 'quality', y = 'alcohol', data = wine)
                bins = (2, 6.5, 8)
                group_names = ['bad', 'good']
                wine['quality'] = pd.cut(wine['quality'], bins = bins, labels = group_names)
                label_quality = LabelEncoder()
                wine['quality'] = label_quality.fit_transform(wine['quality'])
                wine['quality'].value_counts()
                sns.countplot(wine['quality'])
                X = wine.drop('quality', axis = 1)
                y = wine['quality']
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
                sc = StandardScaler()
                X_train = sc.fit_transform(X_train)
                X_test = sc.fit_transform(X_test)
                rfc = RandomForestClassifier(n_estimators=200)
                rfc.fit(X_train, y_train)
                pred_rfc = rfc.predict(X_test)