"""
Created on Sat Mar 27

@author: ktk
"""
from Functions import speak
from Functions import sub
import coden
affirm=["yes","y","Y","Yes","YES"]
def temp():
    while True:
        choice=(input('''Do you want to convert \n1) Celcius to Fahrenheit \n2) Fahrenheit to Celcius \n'''))
        if choice=="1":
            Celsius = int(input("Enter a temperature in Celsius: "))
            Fahrenheit = 9.0/5.0 * Celsius + 32
            sub (f"Temperature: {Celsius} Celsius = {Fahrenheit} F")
        elif choice=="2":
            Fahrenheit = int(input("Enter a temperature in Fahrenheit: "))
            Celsius = ((Fahrenheit-32)*5)/9
            sub (f"Temperature: {Fahrenheit} Fahrenheit = {Celsius} C")
        choice=input("Do you want to try another conversion? ")
        if choice in affirm:
            continue
        else:
            break
def speed():
    while True:
        choice=(input('''Do you want to convert \n1) KM/H to MPH \n2) MPH to KM/H \n'''))
        if choice=="1":
            kmh = float(input("Enter KM/H: "))
            mph = round(kmh/1.609,2)
            sub (f"Speed: {kmh} KM/H = {mph} MPH")        
        elif choice=="2":
            mph = float(input("Enter MPH: "))
            kmh = round(mph*1.609,2)
            sub (f"Speed:{mph} MPH = {kmh} KM/H")   
        choice=input("Do you want to try another conversion? ")
        if choice in affirm:
            continue
        else:
            break
def programunits():
    while True:
        speak("Select initial unit below")
        l=["Decimal","Binary","Octal","Hexadecimal"]
        count=1
        for i in l:
            sub(f"{count} ) {i}")
            count+=1
        start=int(input("Initial unit: "))
        speak("Select final unit: ")
        end=int(input("Final unit: "))
        if start==1:
            sub("Enter decimal value below")
            d=int(input("Enter decimal value: "))
            if end==2:
                sub(f"{d} in decimal has been converted to Binary as {bin(d)}")
            elif end==3:
                sub(f"{d} in decimal has been converted to Octal as {oct(d)}")
            elif end==4:
                sub(f"{d} in decimal has been converted to Hexadecimal as {hex(d)}")
        if start==2:
            sub("Enter binary value below")
            d=(input("Enter binary value: "))
            if end==1:
                sub(f"{d} in binary has been converted to Decimal as {coden.bin_to_int(d)}")
            elif end==3:
                sub(f"{d} in binary has been converted to Octal as {oct(coden.bin_to_int(d))}")
            elif end==4:
                sub(f"{d} in binary has been converted to Hexadecimal as {coden.bin_to_hex(d)}")
        if start==3:
            sub("Enter octal value below")
            d=(input("Enter Octal value: "))
            dd=int(d,8)
            if end==1:
                sub(f"{d} in octal has been converted to Decimal as {dd}")
            elif end==2:
                sub(f"{d} in octal has been converted to Binary as {bin(dd)}")
            elif end==4:
                sub(f"{d} in octal has been converted to Hexadecimal as {hex(dd)}")
        if start==4:
            sub("Enter hexadecimal value below")
            a=(input("Enter Hexadecimal value: "))
            d=coden.hex_to_int(a)
            if end==1:
                sub(f"{d} in Hexadecimal has been converted to Decimal as {d}")
            elif end==2:
                sub(f"{d} in Hexadecimal has been converted to Binary as {bin(d)}")
            elif end==3:
                sub(f"{d} in Hexadecimal has been converted to Octal as {oct(d)}")
        choice=input("Do you want to try another conversion? ")
        if choice in affirm:
            continue
        else:
            break
def units():
    sub("Select a fundamental unit from below")
    print("1. Length (L)\n2. Mass (M)\n3. Time (S)\n4. Current (C)\n5. Amount (A)")
    unit=input("Enter here: ")
    if unit in ["1","L","l","length"]:
        n="metre"
    if unit in ["2","M","m","mass"]:
        n="gram"
    if unit in ["3","S","s","time"]:
        n="seconds"
    if unit in ["4","C","c","current"]:
        n="ampere"
    if unit in ["5","A","a","amount"]:
        n="mole"
    factors=["Kilo","Hecto","","Centi","Milli"]
    count=1
    sub("\nThe supported factors are")
    for i in factors:
        sub(f"{count}. {i+n}")
        count+=1
    speak("Enter initial factor below")
    fac=int(input("Enter serial number for the inital factor: "))
    un=factors[fac-1]+n
    speak(f"Enter inital value in {un}")
    initial=int(input(f"Enter inital value in {un}: "))
    if fac==1:
        metre=initial*1000
    if fac==2:
        metre=initial*100
    if fac==3:
        metre=initial
    if fac==4:
        metre=initial/100
    if fac==5:
        metre=initial/1000
    sub("\nThe units after conversion are: ")
    print(f"!. In Kilo{n} ={metre/1000}")
    print(f"!. In Hecto{n} ={metre/100}")
    print(f"2. In {n} = {metre}")
    print(f"2. In Centi{n} = {metre*100}")
    print(f"2. In Milli{n} = {metre*1000}")
