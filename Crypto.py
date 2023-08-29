# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28

@author: ktk
"""
affirm=["yes","y","Y","Yes"]
def casear():
    def encryptcaesar(code,key):
        result=""
        for i in range(len(code)):
            char=code[i]
            if char.isupper():
                result=result+chr((ord(char)+key-65)%26+65)
            else:
                result=result+chr((ord(char)+key-97)%26+97)
        print("The encrypted result is:",result)
    def decryptcaesar(code,key):
        result=""
        s=26-key
        for i in range(len(code)):
            char=code[i]
            if char.isupper():
                result=result+chr((ord(char)+s-65)%26+65)
            else:
                result=result+chr((ord(char)+s-97)%26+97)
        print("The decrypted result is:",result)
    def caesar():
        while True:
            a=input("Do you want to [E]ncrpyt or [D]ecrypt? ")
            if a=="E" or a=="e":
                code=input("Enter text: ")
                key=int(input("Enter key: "))
                encryptcaesar(code,key)
            elif a=="d" or a=="D":
                code=input("Enter code: ")
                key=int(input("Enter key: "))
                decryptcaesar(code,key)
            leave=input("Do you want to Encrypt/Decrypt another code? ")
            if leave in affirm:
                continue
            else:
                break
def vigenre():           
    def generateKey(string,key):
    	key=list(key)
    	if len(string)==len(key):
    		return(key)
    	else:
    		for i in range(len(string)-len(key)):
    			key.append(key[i%len(key)])
    	return("" .join(key))
    def cipherText(string, key):
    	cipher_text = []
    	for i in range(len(string)):
    		x = (ord(string[i])+ord(key[i]))%26
    		x += ord('A')
    		cipher_text.append(chr(x))
    	return("" .join(cipher_text))
    def originalText(cipher_text, key):
    	orig_text = []
    	for i in range(len(cipher_text)):
    		x = (ord(cipher_text[i])-ord(key[i])+26)%26
    		x += ord('A')
    		orig_text.append(chr(x))
    	return("" .join(orig_text))
    def VigenreCipher():
        while True:
            a=input("Do you want to [E]ncrpyt or [D]ecrypt? ")
            if a=="E" or a=="e":
                string=input("Enter Text: ")
                keyword=input("Enter Keyword: ")
                key=generateKey(string, keyword)
                cipher_text=cipherText(string,key)
                print("The encrypted result is:",cipher_text)
            elif a=="d" or a=="D":
                 string=input("Enter Text: ")
                 keyword=input("Enter Keyword: ")
                 key=generateKey(string, keyword)
                 cipher_text=cipherText(string,key)
                 print("The decrypted result is:",originalText(cipher_text,key))
            leave=input("Do you want to Encrypt/Decrypt another code? ")
            if leave in affirm:
                continue
            else:
                break
def guesspin():
    digits = input("Enter the four digits from the PIN without any separators: ")
    PINs = []
    for a in range(4): # 1234
      for b in range(4): # 1234
        if a != b:
          for c in range(4):
            if c != a and c != b:
              for d in range(4):
                if d != a and d != b and d != c:
                  PIN = digits[a]+digits[b]+digits[c]+digits[d]
                  if PIN not in PINs:
                    print(PIN)
                    PINs.append(PIN)
    print(f"\nThere are {len(PINs)} possible PINs.")
def morsecode():
    code = (".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..")
    digit = ("-----",".----","...--","....-",".....","-....","--...","---..","----.")
    option = ""
    while option not in ("D","E"):
      option = input("Enter 'E' to encode and 'D' to decode: ").upper()
    if option == "E":
      morse = ""
      text = input("Please enter the text to be encoded: ").upper()
      for char in text:
        if char >= "A" and char <= "Z":
          morse += (code[ord(char)-65] + " ")
        if char >= "0" and char <= "9":
          morse += (digit[eval(char)] + " ") 
        if char == " ":
          morse += "| "
      print(morse)
    else:
      morse = input("Enter the morse code: ").split()
      text = ""
      for cluster in morse:
        if cluster in code:
          text += chr(code.index(cluster)+65)
        if cluster in digit:
          text += str(digit.index(cluster))
        if cluster == "|":
          text += " "
      print(text)
