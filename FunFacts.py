# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28

@author: ktk
"""
import math as m,random
from Functions import speak
from Functions import sub
def get_super(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)
affirm=["yes","y","Y","Yes"]  
def funfact():
    facts1=["Legendre Conjecture","Sieve of Eratosthenes","Collatz Conjecture"]
    fact=random.choice(facts1)
    if fact==facts1[0]:
        print(facts1[0])
        sub("\nLegendre Conjecture says that there is always one prime number between sqaures of any two consecutive natural numbers.\n")
        speak("Do you know what a conjecture is?")
        doubt=input("ps. Do you kno what a conjecture is? ")
        if doubt in affirm:
            sub("Ah cool, you're actually pretty smart.")
            sub("Let's try it out once.")
        else:
            sub("Okay,so a conjecture is a proposition or conclusion based upon incompleate information to which no proof has been found i.e it has not been proved or disproved.\n")
            sub("for example...")
        speak("Enter a natural number below:")
        n=int(input("Enter a natural number 'n' : "))
        a=get_super("2")
        sub(f"On trying to find prime numbers between n{a} = {n*n} and (n+1) {a} = {(n+1)**2} we get:")
        def isprime( n ):
        	i = 2
        	for i in range (2, int((m.sqrt(n)+1))):
        		if n%i == 0:
        			return False
        	return True
        def LegendreConjecture( n ):
        	for i in range (n*n, (((n+1)*(n+1))+1)):
        		if(isprime(i)):
        			print (i)
        LegendreConjecture(n)
    if fact==facts1[1]:
        l=[]
        sub(facts1[1])
        speak("Do you kno what the Sieve of Eratosthenes is?")
        doubt=input("Do you kno what the Sieve of Eratosthenes is? ")
        if doubt in affirm:
            sub("Ah cool, you're actually pretty smart.")
            sub("Let's try it out once.")
        else:
            sub("The sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to any given limit.\n")
            sub("for example...")
        speak("Enter a number below:")
        n=int(input("Enter a number: "))
        def sieveoferatosthenes(n):
            for i in range(0, n+1):
                if i>1:
                    for j in range(2,i):
                        if(i % j==0):
                            break
                        else:
                            if i in l:
                                pass
                            else:
                                l.append(i)
        sieveoferatosthenes(n)
        if len(l)==0:
            sub("Oops! It looks like there are no prime numbers in the given range.")
        sub(f"The prime numbers smaller than or equal to {n} are {l}")
    if fact==facts1[2]:
        speak("Do you kno what the Collatz Conjecture is?")
        doubt=input("Do you kno what the Collatz Conjecture is? ")
        if doubt in affirm:
            sub("Ah cool, you're actually pretty smart.")
            sub("Let's try it out once.")
        else:
            sub("The Collatz conjecture is a conjecture that a particular sequence always reaches 1. The sequence is defined as: start with a number n. The next number in the sequence is n/2 if n is even and 3n + 1 if n is odd.\n")
            sub("for example...")
        def collatz(n):
            while n > 1:
                print(n, end=' ')
                if (n % 2):
                    n = 3*n + 1
                else:
                    n = n//2
            print(1, end='')
        speak("Enter a number below")
        n = int(input('Enter a number: '))
        print('Sequence:')
        collatz(n)
