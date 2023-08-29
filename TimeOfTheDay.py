"""
Created on Thu Mar 25 

@author: ktk
"""
import time as t
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from datetime import date
from Functions import speak
from Functions import sub
time=datetime.now()
current_time = time.strftime("%H:%M:%S")
def chronos(name):
    a=int(current_time[0:2])
    if a>=7 and a<12:
        g="Good morning "+str(name)
    elif a>=12 and a<16:
        g="Good afternoon "+str(name)
    else:
        g="Good evening "+str(name)
    return(g)
def goodbye(name):
    a=int(current_time[0:2])
    if a>=7 and a<16:
        g="Hope you have a good day!! "+str(name)
    else:
        g='''Goodnight buddy!!
        Sweet dreams '''+str(name)
    return(g)
def now():
    sub("The time now is",current_time)
def stopwatch():
    starttime=t.time()
    lasttime=starttime
    lapnum=1
    sub("Press ENTER to count laps.\nPress CTRL+C to stop.")
    try:
        while True:
            input()
            laptime=round((t.time()-lasttime),2)
            totaltime=round((t.time()-starttime),2)
            sub(f"Lap No. {str(lapnum)}")
            sub(f"Total Time: {str(totaltime)}")
            sub(f"Lap Time: {str(laptime)}")
            print("*"*20)
            lasttime=t.time()
            lapnum+=1
    except KeyboardInterrupt:
        totaltime=round((t.time()-starttime),2)
        sub(f"Total Time: {str(totaltime)}")
        print("*"*20)
        sub("Done")
def timer():
    ch=int(input("Do you want a\n1)Simple Timer\n2)Timer 2.0: "))
    if ch==1:
        def countdown(t2):
            while t2:
                mins, secs = divmod(t2, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                sub(timer)
                t.sleep(1)
                t2 -= 1
            sub('Fire in the hole!!')
        t2 = input("Enter the time in seconds: ")
        countdown(int(t2))
    elif ch==2:
        root = Tk()
        root.geometry("300x250")
        root.title("Time Counter")
        hour=StringVar()
        minute=StringVar()
        second=StringVar()
        hour.set("00")
        minute.set("00")
        second.set("00")
        hourEntry= Entry(root, width=3, font=("Arial",18,""),
        				textvariable=hour)
        hourEntry.place(x=80,y=20)
        minuteEntry= Entry(root, width=3, font=("Arial",18,""),
        				textvariable=minute)
        minuteEntry.place(x=130,y=20)
        secondEntry= Entry(root, width=3, font=("Arial",18,""),
        				textvariable=second)
        secondEntry.place(x=180,y=20)
        def submit():
        	try:
        		temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
        	except:
        		sub("Please input the right value")
        	while temp >-1:
        		mins,secs = divmod(temp,60)
        		hours=0
        		if mins >60:
        			hours, mins = divmod(mins, 60)
        		hour.set("{0:2d}".format(hours))
        		minute.set("{0:2d}".format(mins))
        		second.set("{0:2d}".format(secs))
        		root.update()
        		t.sleep(1)
        		if (temp == 0):
        			messagebox.showinfo("Time Countdown", "Time's up!! ")
        		temp -= 1
        btn = Button(root, text='Set Time Countdown', bd='5',
        			command= submit)
        btn.place(x = 70,y = 120)
        root.mainloop()