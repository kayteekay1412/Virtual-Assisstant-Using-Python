"""
Created on Thu Mar 25 

@author: ktk
"""
# THIS IS IT
import TimeOfTheDay as t
import Games
import IPaddress as ip
import Conversions as convert
import Calculator as c
import Crypto as crypt
import FunFacts as fun
import Internet as net
import Functions as func
import General as gen
from Functions import sub
used=1
while True:
    k=input("[TAP A KEY TO ACTIVATE] ")
    if k=="0":
        sub("Thank you for using ktk!")
        break
    else:
        if used==0:
            net.otp()
        func.clear()
        func.speak("How can I help you?")
        com=func.hear()
        comms=com.lower()
        if 'wikipedia' in comms:
            net.wikisearch()
        elif "google search" in comms:
            net.gsearch()