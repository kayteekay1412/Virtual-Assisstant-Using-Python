# -*- coding: utf-8 -*-
"""
Created on Sat May 15

@author: ktk
"""

# GENERAL

import os,random,calendar,time
from win10toast import ToastNotifier
from Functions import speak,sub
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])

affirm=["yes","y","Y","Yes","YES"]

def music():
    music_dir = 'D:\\ktk\\music'
    songs = os.listdir(music_dir)
    print("Playlist:\n")
    for i in range(len(songs)):
        print(i+1,")",songs[i])
    speak("Do you want to play any particular song? ")
    s=input("Do you want to play any particular song? ")
    if s in ["NO","no","No","n","N"]:
        speak("Let me play a random song then...")
        a=random.randint(0,len(songs))
        os.startfile(os.path.join(music_dir,songs[a]))
    elif s in ["Yes","yes","Y","y","YES"]:
        c=input("Which song do you want to play?\n[ENTER THE NUMBER OF THE SONG YOU WISH TO PLAY] ")
        os.startfile(os.path.join(music_dir, songs[int(c)]))
def coolfont():
    while True:
        speak("Do you want to see something cool?")
        speak("Enter some text below")
        text=input("Enter the text: ")
        lngth = len(text)
        for x in range(0,lngth):
            c = text[x]
            c = c.upper()
            if (c == "A"):
                print("..######..\n..#....#..\n..######..", end = " ")
                print("\n..#....#..\n..#....#..\n\n")
            elif (c == "B"):
                print("..######..\n..#....#..\n..#####...", end = " ")
                print("\n..#....#..\n..######..\n\n")
            elif (c == "C"):
                print("..######..\n..#.......\n..#.......", end = " ")
                print("\n..#.......\n..######..\n\n")
            elif (c == "D"):
                print("..#####...\n..#....#..\n..#....#..", end = " ")
                print("\n..#....#..\n..#####...\n\n")
            elif (c == "E"):
                print("..######..\n..#.......\n..#####...", end = " ")
                print("\n..#.......\n..######..\n\n")
            elif (c == "F"):
                print("..######..\n..#.......\n..#####...", end = " ")
                print("\n..#.......\n..#.......\n\n")
            elif (c == "G"):
                print("..######..\n..#.......\n..#.####..", end = " ")
                print("\n..#....#..\n..#####...\n\n")
            elif (c == "H"):
                print("..#....#..\n..#....#..\n..######..", end = " ")
                print("\n..#....#..\n..#....#..\n\n")
            elif (c == "I"):
                print("..######..\n....##....\n....##....", end = " ")
                print("\n....##....\n..######..\n\n")
            elif (c == "J"):
                print("..######..\n....##....\n....##....", end = " ")
                print("\n..#.##....\n..####....\n\n")
            elif (c == "K"):
                print("..#...#...\n..#..#....\n..##......", end = " ")
                print("\n..#..#....\n..#...#...\n\n")
            elif (c == "L"):
                print("..#.......\n..#.......\n..#.......", end = " ")
                print("\n..#.......\n..######..\n\n")
            elif (c == "M"):
                print("..#....#..\n..##..##..\n..#.##.#..", end = " ")
                print("\n..#....#..\n..#....#..\n\n")
            elif (c == "N"):
                print("..#....#..\n..##...#..\n..#.#..#..", end = " ")
                print("\n..#..#.#..\n..#...##..\n\n")
            elif (c == "O"):
                print("..######..\n..#....#..\n..#....#..", end = " ")
                print("\n..#....#..\n..######..\n\n")
            elif (c == "P"):
                print("..######..\n..#....#..\n..######..", end = " ")
                print("\n..#.......\n..#.......\n\n")
            elif (c == "Q"):
                print("..######..\n..#....#..\n..#.#..#..", end = " ")
                print("\n..#..#.#..\n..######..\n\n")
            elif (c == "R"):
                print("..######..\n..#....#..\n..#.##...", end = " ")
                print("\n..#...#...\n..#....#..\n\n")
            elif (c == "S"):
                print("..######..\n..#.......\n..######..", end = " ")
                print("\n.......#..\n..######..\n\n")
            elif (c == "T"):
                print("..######..\n....##....\n....##....", end = " ")
                print("\n....##....\n....##....\n\n")
            elif (c == "U"):
                print("..#....#..\n..#....#..\n..#....#..", end = " ")
                print("\n..#....#..\n..######..\n\n")
            elif (c == "V"):
                print("..#....#..\n..#....#..\n..#....#..", end = " ")
                print("\n...#..#...\n....##....\n\n")
            elif (c == "W"):
                print("..#....#..\n..#....#..\n..#.##.#..", end = " ")
                print("\n..##..##..\n..#....#..\n\n")
            elif (c == "X"):
                print("..#....#..\n...#..#...\n....##....", end = " ")
                print("\n...#..#...\n..#....#..\n\n")
            elif (c == "Y"):
                print("..#....#..\n...#..#...\n....##....", end = " ")
                print("\n....##....\n....##....\n\n")
            elif (c == "Z"):
                print("..######..\n......#...\n.....#....", end = " ")
                print("\n....#.....\n..######..\n\n")
            elif (c == " "):
                print("..........\n..........\n..........", end = " ")
                print("\n..........\n\n")
            elif (c == "."):
                print("----..----\n\n")
        play_again=input("Do you want to try this again? ")
        if play_again in affirm:
            continue
        else:
            break
def sortwords():
    while True:
        sub("enter the string of words to be sorted below.")
        string = input("Enter a string: ")
        words = [word.lower() for word in string.split()]
        words.sort()
        sub("The sorted words are:")
        for word in words:
           sub(word)
        play_again=input("Do you want to sort another string? ")
        if play_again in affirm:
            continue
        else:
            break
def grocerylist():
    while True:
    	try:
            	speak("Enter budet below")
            	bg = float(input("Enter your budget : "))
            	s = bg
    	except ValueError:
    		sub("PRINT BUDGET AS AN AMOUNT")
    		continue
    	else:
    		break
    a ={"name":[], "quant":[], "price":[]}
    b = list(a.values())
    na = b[0]
    qu = b[1]
    pr = b[2]
    while True:
    	try:
    		ch = int(input("1.ADD\n2.EXIT\nEnter your choice : "))
    	except ValueError:
    		sub("\nERROR: Choose only digits from the given option")
    		continue
    	else:
    		if ch == 1 and s>0:
    			speak("Enter product name below")				
    			pn = input("Enter product name : ")
    			speak(f"Enter quantity of {pn} below")
    			q = input("Enter quantity : ")
    			speak(f"Enter price of {pn} below")
    			p = float(input("Enter price of the product : "))
    			if p*q>s:
    				sub("\nCAN'T BUY THE PRODUCT")
    				continue
    			else:
    				if pn in na:
    					ind = na.index(pn)
    					qu.remove(qu[ind])
    					pr.remove(pr[ind])
    					qu.insert(ind, q)
    					pr.insert(ind, p)
    					s = bg-sum(pr)
    					sub(f"\namount left {s}")
    				else:
    					na.append(pn)
    					qu.append(q)
    					pr.append(p)
    					s = bg-sum(pr)
    					sub(f"\namount left {s}")
    		elif s<= 0:
    			sub("\nNO BUDGET")
    		else:
    			break
    sub(f"\nAmount left : Rs. {s}")
    if s in pr:
    	sub(f"\nAmount left can buy you a {na[pr.index(s)]}")
    sub("\n\n\nGROCERY LIST")
    for i in range(len(na)):
    	sub(f"{na[i]} {qu[i]} {pr[i]}")
def calender():
    speak("Please Enter the year below")
    year = int(input("Please Enter the year: "))
    speak("Please Enter the month in numbers below")
    month = int(input("Please Enter the month: "))
    print()
    print(calendar.month(year, month))
def desktopreminder():
    toaster = ToastNotifier()
    try:
        speak("Enter title of the reminder below")
        title=input("Title of reminder: ")
        speak("Enter the reminde below")
        text=input("Message of reminder: ")
        speak("After how much time do you want the reminder?")
        time_min=input("In how many minutes? ")
        time_min=float(time_min)
    except:
        speak("Enter title of the reminder below")
        title = input("Title of reminder\n")
        speak("Enter the reminde below")
        text = input("Message of remindar\n")
        speak("After how much time do you want the reminder?")
        time_min=float(input("In how many minutes?\n"))
    time_min = time_min * 60
    speak("\nSetting up reminder..")
    time.sleep(2)
    speak("\nall set!")
    time.sleep(time_min)
    toaster.show_toast(f"{title}",f"{text}",duration=10,threaded=True)
    while toaster.notification_active(): 
        time.sleep(0.005)     
def seriesrating():
    l=[]
    a=1
    count=1
    while a>0:
        num=(input(f"Enter the views for the {ordinal(count)} episode (in millions): "))
        if num!="":
            num=float(num)
            l.append(num)
            count+=1
        elif num=="":
            a=0
    ll=len(l)
    view=(round((sum(l))/ll),2)
    print(f"Over {count} episodes, the average viewers (in millions) is: {view}")