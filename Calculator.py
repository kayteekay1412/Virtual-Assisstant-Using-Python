# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27

@author: ktk
"""
from datetime import date
import numpy as np
import math as m
affirm=["yes","y","Y","Yes","YES"]
from Functions import speak
from Functions import sub
def get_super(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)
def power():
    speak("Enter the base number below")
    n=int(input("Enter the base number: "))
    speak("Enter the power below")
    m=int(input("Enter the power below: "))
    sub(f"{n} raised to the power {m} is {n**m}")
def matrix():
    sub("1) Add 2 matrices\n2) Transpose a Matrix\n3) Multiply 2 matrices")
    op=int(input("Operation: "))
    if op==1:
        R1 = int(input("Enter the number of rows in the matrix A: "))
        C1 = int(input("Enter the number of columns in the Matrix A: "))
        R2 = int(input("Enter the number of rows in the matrix B: "))
        C2 = int(input("Enter the number of columns in the Matrix A: "))
        if C1==R1:
            X=[]
            Y=[]
            sub("Enter the entries rowwise for Matrix A:")
            for i in range(R1):
                a =[]
                for j in range(C1):
                    aa=int(input("Enter an element: "))
                    a.append(aa)
                X.append(a)
            print()
            sub("Enter the entries rowwise for Matrix B:")
            for i in range(R2):
                a =[]
                for j in range(C2):
                    aa=int(input("Enter an element: "))
                    a.append(aa)
                Y.append(a)
        result = [[X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]
        sub("The sum of the matrices are:")
        for r in result:
           print(r)
    if op==2:
        R1 = int(input("Enter the number of rows in the matrix: "))
        C1 = int(input("Enter the number of columns in the Matrix: "))
        X=[]
        sub("Enter the entries rowwise for Matrix:")
        for i in range(R1):
            a =[]
            for j in range(C1):
                aa=int(input("Enter an element: "))
                a.append(aa)
            X.append(a)
        result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
        sub("The transpose of the given matrix is:")
        for r in result:
           print(r)
    if op==3:
        R1 = int(input("Enter the number of rows in the matrix A: "))
        C1 = int(input("Enter the number of columns in the Matrix A: "))
        R2 = int(input("Enter the number of rows in the matrix B: "))
        C2 = int(input("Enter the number of columns in the Matrix A: "))
        if C1==R1:
            matrixA=[]
            matrixB=[]
            sub("Enter the entries rowwise for Matrix A:")
            for i in range(R1):
                a =[]
                for j in range(C1):
                    aa=int(input("Enter an element: "))
                    a.append(aa)
                matrixA.append(a)
            print()
            sub("Enter the entries rowwise for Matrix B:")
            for i in range(R2):
                a =[]
                for j in range(C2):
                    aa=int(input("Enter an element: "))
                    a.append(aa)
                matrixB.append(a)
        elif C1!=R1:
            sub("In order for matrix multiplication to be defined, the number of columns in the first matrix must be equal to the number of rows in the second matrix.")
        res = np.dot(matrixA,matrixB)
        sub("The product of the two matrices are:")
        for i in res:
            print(i)
def multiples():
    speak("Enter the number whose multiples are required?")
    num = int(input("Enter the number whose multiples are required? "))
    speak("How many multiples are required")
    a=int(input("How many multiples are required? "))
    print()
    for i in range(1, a+1):
       speak(f"{num} times {i} = {num*i}")
       print(f"{num} x {i} = {num*i}")
def calculate():
    def addition ():
        sub("Addition")
        n = float(input("Enter the number: "))
        t = 0 
        ans = 0
        while n != 0:
            ans = ans + n
            t+=1
            n = float(input("Enter another number (0 to calculate): "))
        return [ans,t]
    def subtraction ():
        sub("Subtraction");
        n = float(input("Enter the number: "))
        t = 0 
        sum = 0
        while n != 0:
            sum = sum - n
            t+=1
            n = float(input("Enter another number (0 to calculate): "))
        return [sum,t]
    def multiplication ():
        sub("Multiplication")
        n = float(input("Enter the number: "))
        t = 0 
        ans = 1
        while n != 0:
            ans = ans * n
            t+=1
            n = float(input("Enter another number (0 to calculate): "))
        return [ans,t]
    def average():
        sub("Average")
        an = []
        an = addition()
        t = an[1]
        a = an[0]
        ans = a / t
        return [ans,t]
    while True:
        list = []
        print("")
        sub("Simple Calculator")
        sub("Enter 'a' for addition")
        sub("Enter 's' for substraction")
        sub("Enter 'm' for multiplication")
        sub("Enter 'v' for average")
        sub("Enter 'q' for quit")
        c = input(" ")
        if c != 'q':
            if c == 'a':
                list = addition()
                print("Ans = ", list[0], " total inputs ",list[1])
            elif c == 's':
                list = subtraction()
                print("Ans = ", list[0], " total inputs ",list[1])
            elif c == 'm':
                list = multiplication()
                print("Ans = ", list[0], " total inputs ",list[1])
            elif c == 'v':
                list = average()
                print("Ans = ", list[0], " total inputs ",list[1])
            else:
                print ("Sorry, invilid character")
        else:
            break
def factor():
    while True:
        def check(n): 
        	for i in range(2,n): 
        		if n%i == 0: 
        			return False 
        	return True 
        n = int(input("Enter the Number: ")) 
        print(str(n)+" = ",end='') 
        for i in range (2,n+1): 
        	c = 0 
        	if check(i) == True: 
        		while True: 
        			if(n%i == 0): 
        				n /= i 
        				c+= 1 
        			else: 
        				break 
        		if c == 1: 
        			print(str(i)+" x ",end='') 
        		elif c !=0: 
        			print(str(i)+get_super(str(c))+" x ",end='') 
        print(" \b\b\b ")
        speak("Do you want to facroeize another number?")
        choice=input("Do you want to factorize another number? ")
        if choice in affirm:
            continue
        else:
            break
def factorial():
    while True:
        speak("Enter the number whose factorial is desired")
        n=int(input("Enter the number whose fatorial is desired: "))
        sub(f"The factorial of {n} is {m.factorial(n)}")
        choice=input("Do you want to try another factorial? ")
        if choice in affirm:
            continue
        else:
            break
def si():
    while True:
        speak("To calculate simple interest")
        p=float(input("Please enter the principal amount: "))
        r=float(input("Please enter the rate of interest: "))
        t=float(input("Please enter the time period: "))
        s=(p*r*t)/100
        sub(f"The simple interest is {s}")
        sub(f"The total money, at the end of {t} years is {p+s}")
        choice=input("Do you want to try another simple interest calculation? ")
        if choice in affirm:
            continue
        else:
            break
def ci():
    while True:
        speak("To calculate compound interest")
        p=float(input("Please enter the principal amount: "))
        r=float(input("Please enter the rate of interest: "))
        t=float(input("Please enter the time period: "))
        aa=p*(pow((1+r)/100),t)
        sub(f"The compound interest is {t-p}")
        sub(f"The total money, at the end of {t} years is {aa}")
        choice=input("Do you want to try another compound interest calculation? ")
        if choice in affirm:
            continue
        else:
            break
def allprime():
    while True:
        speak("To find prime numbers in a given range")
        start=int(input("Please enter the initial value: "))
        end=int(input("Please enter the ultimate value: "))
        l=[]
        for i in range(start, end+1):
            if i>1:
                for j in range(2,i):
                    if(i % j==0):
                        break
                    else:
                        if i in l:
                            pass
                        else:
                            l.append(i)
        sub(f"The prime numbers between {start} and {end} are:")
        for i in l:
              print(i)
        if len(l)==0:
            sub("Oops! It looks like there are no prime numbers in the given range.")
        choice=input("Do you want to find more prime numbers? ")
        if choice in affirm:
            continue
        else:
            break
def fibonacci():
    ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
    n1,n2,count=0,1,0
    fibonacci=[]
    while True:
        speak("Do you want to display n terms of Fibonacci Sequence or display a specific term in the sequence")
        a=int(input("Do you want to display \n1)the Fibonacci Sequence upto a term\n2)a specific term in the sequence "))
        if a==1:
            speak("How many terms do you want to display?")
            n=int(input("How many terms do you want to display? "))
        elif a==2:
            speak("Which term do you want?")
            n=int(input("Which term do you want? "))
        if n<=0:
            sub("Please enter a positive integer")
        elif n==1:
            print("1")
        else:
            if a==1:
                sub("Fibonacci Sequence:")
                while count<n:
                    print(n1)
                    nth=n1+n2
                    n1,n2=n2,nth
                    count+=1
            elif a==2:
                while count<n:
                    fibonacci.append(n1)
                    nth=n1+n2
                    n1,n2=n2,nth
                    count+=1
                sub(f"The {ordinal(n)} term of the Fibonacci Sequence is {fibonacci[n-1]}")
        choice=input("Do you want to run the Fibonnaci Sequence again? ")
        if choice in affirm:
            continue
        else:
            break
def quadratic():
    while True:
        speak("To calculate solutions of quadratic equation: ")
        q="x"+get_super("2")
        a=int(input(f"Enter the coefficient of {q}: "))
        b=int(input("Enter the coefficient of x: "))
        c=int(input("Enter the constant term: "))
        d=(b**2)-(4*a*c)
        if d>0:
            speak("The given equation has 2 distinct roots.")
            x1=(b*(-1))+m.sqrt(d)
            x2=(b*(-1))-m.sqert(d)
            sub(f"First root: {x1}")
            sub(f"Second root: {x2}")
        elif d==0:
            speak("The given equation has 2 equal roots")
            x1=(b*(-1))+m.sqrt(d)
            sub(f"The root of the given equation is: {x1}")
        elif d<0:
            speak("The given equation has imginary roots. I can't solve them at the moment.")
        choice=input("Do you want to solve more quadratic equations? ")
        if choice in affirm:
            continue
        else:
            break
def floydtriangle():
    speak("Enter the number of rows below")
    rows=int(input("Please Enter the total Number of Rows: "))
    number = 1
    sub("Floyd's Triangle\n")
    for i in range (1,rows+1):
        for j in range (1,i+1):        
            print(number,end='  ')
            number=number+1
        print()    
def geometry():
    shapes=["cirlce","triangle","trapezoid","parallelogram","rectangle","rhombus","sphere","cylinder","cube","cone","cuboid"]
    count=1
    for i in shapes:
        print(f"{count}) {i}")
        count+=1
    speak("Enter the serial number of the shape below")
    shape=int(input("Enter the serial number of the shape: "))
    if shape==1:
        r=float(input("Enter the radius of the circle: "))
        sub(f"The circle of radius {r} has:\n1) Diameter = {r*2}\n2) Circumference = {2*(m.pi)*r}\n3) Area = {(m.pi)*(r**2)}")
    elif shape==2:
        triangles=["Equilateral","Isoceles","Scalene","Right-Angled","Unknown"]
        count=1
        for i in triangles:
            print(f"{count} ) {i}")
        speak("Enter the type of triangle below")
        types=int(input("Enter serial number of triangle: "))
        if types==1:
            side = float(input('Please Enter Length of any side of the Equilateral Triangle: '))
            Perimeter=3*side
            sub(f"Area of the Equilateral Triangle = {(m.sqrt(3)/4)*(side*side)}")
            sub(f"Perimeter of the Equilateral Triangle = {Perimeter}")
            sub(f"Semi Perimeter of the Equilateral Triangle = {Perimeter/2}")
            sub(f"Altitude of the Equilateral Triangle = {(m.sqrt(3)/2)*side}")
        elif types==2:
            a = float(input("Enter the Isosceles Triangle Side Length  : "))
            b = float(input("Enter the Other Side of Isosceles Triangle : "))         
            sub(f"The Perimeter of the Isosceles Triangle = {(2*a)+b}")
            sub(f"The Area of the Isosceles Triangle = {(b*m.sqrt((4*a*a)-(b*b)))/4}")
        elif types==3:
            sub("Do you have the height and base?")
            sub("[PRESS Y FOR YES AND N FOR NO]")
            ch=input("ENTER: ")
            if ch=="Y":
                b = float(input('Please Enter the Base of a Triangle: '))
                h = float(input('Please Enter the Height of a Triangle: '))
                sub(f"The Area of a Triangle using base ({b}) and height ({h}) = {(b*h) / 2}")
            elif ch=="N":
                a = float(input('Please Enter the First side of a Triangle: '))
                b = float(input('Please Enter the Second side of a Triangle: '))
                c = float(input('Please Enter the Third side of a Triangle: '))
                p = a+b+c
                s = p/2
                sub(f"\nThe Perimeter of Traiangle = {p}")
                sub(f" The Semi Perimeter of Traiangle = {s}")
                sub(f" The Area of a Triangle = {(s*(s-a)*(s-b)*(s-c))**(0.5)}")
        elif types==4:
            speak("Enter the base and height of the triangle below")
            h=float(input("Please Enter the Height of the Right Triangle: "))
            b=float(input("Please Enter the Base of the Right Triangle: "))
            c=m.sqrt((h**2)+(b**2))
            sub(f"The Perimeter of the given Right Triangle = {h+b+c}")
            sub(f"The Area of the given Right Triangle = {0.5*b*h}")
        elif types==5:
            speak("Enter the lengths of the triangle below")
            a=float(input("Length of 1st side: "))
            b=float(input("Length of 2nd side: "))
            c=float(input("Length of 3rd side: "))
            if a==b and b==c and a==c:
                tri="Equilateral"
            elif a==b and b!=c:
                tri="Isoceles"
            elif b==c and c!=a:
                tri="Isoceles"
            elif c==a and a!=b:
                tri="Isoceles"
            else:
                tri="Scalene"
            p = a+b+c
            s = p/2
            sub(f"The given triangle is {tri}")
            sub(f"Area of given triangle = {(s*(s-a)*(s-b)*(s-c))**(0.5)}")
    elif shape==3:
        speak("Enter the value for two bases and corresponding height of the Trapezoid below")
        b1=float(input('Please Enter the First Base of a Trapezoid: '))
        b2=float(input('Please Enter the Second Base of a Trapezoid: '))
        h=float(input('Please Enter the Height of a Trapezoid: '))
        sub(f"\n Area of a Trapezium = {0.5*(b1+b2)*h}")
        sub(f"Median of a Trapezium = {0.5*(b1+b2)}")
    elif shape==4:
        speak("Enter the values of base and height of Parallelogram below")
        b=float(input("PLease Enter the Base of Parallelogram: "))
        h=float(input("Please Enter the Height of Parallelogram: "))
        sub(f"The Area of Parallelogram of Base {b} and height {h} = {b*h}")
    elif shape==5:
        speak("Enter the length and Breadth of Rectangle below")
        l=float(input("Please Enter the length of the Rectangle: "))
        b=float(input("Please Enter the breadth of the Rectangle: "))
        sub(f"The Perimeter of the given Rectangle = {2*(l+b)}")
        sub(f"The Area of the given Rectangle = {l*b}")
    elif shape==6:
        speak("Enter the value of the diagonals of the rhombus below")
        d1=float(input("Please Enter Rhombus' First Diagonal  = "))
        d2=float(input("Please Enter Rhombus' Second Diagonal = "))
        sub(f"The Perimeter of the given Rhombus = {2*(m.sqrt((d1**2)+(d2**2)))}")
        sub(f"The Area of a Rhombus = {(d1*d2)/2}")
    elif shape==7:
        speak("Enter the radius of the sphere below")
        r=float(input("Please Enter the Radius of the Sphere: "))
        sub(f"The Surface Area of the given Sphere = {4*(m.pi)*(r**2)}")
        sub(f"The Volume of the given Sphere = {(4/3)*(m.pi)*(r**3)}")
    elif shape==8:
        speak("Enter the radius and height of the cylinder below")
        r=float(input("Please Enter the Radius of the Cylinder: "))
        h=float(input("Please Enter the Height of the Cylinder: "))
        sub(f"The Surface Area of the cylinder = {2*(m.pi)*r*(r+h)}")
        sub(f"The Lateral Surface Area (LSA) of the Cylinder = {2*r*h*(m.pi)}")
        sub(f"The Total Surface Area (TSA) of the Cylinder = {(2*r*h*(m.pi))+(2*(m.pi)*(r**2))}")
        sub(f"The Volume of the Cylinder = {(m.pi)*(r**2)*h}")
    elif shape==9:
        speak("Enter the length of the side of the Cube below")
        l=float(input("Please Enter the Length of any side of a Cube: "))
        sub(f"\nThe Surface Area of the Cube = {6*(l*l)}")
        sub(f"The Lateral Surface Area of the Cube = {4*(l*l)}")
        sub(f"The Volume of the Cube = {l**3}")
    elif shape==10:
        speak("Enter the radius and height of the Cone below")
        r = float(input('Please Enter the Radius of a Cone: '))
        h = float(input('Please Enter the Height of a Cone: '))
        l = m.sqrt((r**2)+(h**2))
        sub(f"\nThe Length of a Side (Slant)of a Cone = {l}")
        sub(f"The Surface Area of a Cone = {(m.pi)*r*(r+1)}")
        sub(f"The Lateral Surface Area of a Cone = {(m.pi)*r*l}")
        sub(f"The Volume of a Cone = {(1/3)*(m.pi)*(r**2)*h}")
    elif shape==11:
        speak("Enter the length, widht and height of the Cuboid below")
        l = float(input('Please Enter the Length of a Cuboid: '))
        w = float(input('Please Enter the Width of a Cuboid: '))
        h = float(input('Please Enter the Height of a Cuboid: '))
        sub(f"\nThe Surface Area of the Cuboid = {2*((l*w)+(w*h)+(h*l))}")
        sub(f"The Lateral Surface Area of the Cuboid = {2*h*(l+w)}")
        sub(f"The Volume of the Cuboid = {l*b*h}")
def leapornot():
    while True:
        speak("Enter an year to determine whether it is leap or not")
        y=int(input("Enter an year: "))
        if y%4==0:
           if y%100==0:
               if y%400==0:
                   sub("{0} is a leap year".format(y))
               else:
                   sub("{0} is not a leap year".format(y))
           else:
               sub("{0} is a leap year".format(y))
        else:
           sub("{0} is not a leap year".format(y))
        choice=input("Do you want to check for another year?? ")
        if choice in affirm:
            continue
        else:
            break
def daysbetween():
    while True:
        speak("Enter the intial and final date")
        a=input("Enter Initial Date [space] Month [space] Year: ")
        b=input("Enter Final Date [space] Month [space] Year: ")
        day1=int(a[0:2])
        month1=int(a[3:6])
        year1=int(a[6:12])
        day2=int(b[0:2])
        month2=int(b[3:6])
        year2=int(b[6:12])
        f_date = date(year1, month1, day1)
        l_date = date(year2, month2, day2)
        delta = l_date - f_date
        sub(f"The number of days between Initial and Final dates is: {delta.days}")
        choice=input("Do you want to calculate for another pair of dates?? ")
        if choice in affirm:
            continue
        else:
            break
def daysleftinmonth():
    while True:
        speak("Enter the date to find the number of days left in the month")
        a=input("Enter Initial Date [space] Month [space] Year: ")
        day=int(a[0:2])
        month=int(a[3:6])
        year=int(a[6:12])
        if (year % 4) == 0:
           if (year % 100) == 0:
               if (year % 400) == 0:
                   a=1
               else:
                   a=0
           else:
               a=1
        else:
            a=0
        l1,l2,l3=[1,3,5,7,8,10,12],[4,6,9,11],[2]
        if month in l1:
            sub(f"There are {31-day} days left in the current month.")
        elif month in l2:
            sub(f"There are {30-day} days left in the current month.")
        elif month in l3:
            if a==1:
                sub(f"There are {29-day} days left in the current month.")
            elif a==0:
                sub(f"There are {28-day} days left in the current month.")
        choice=input("Do you want to check for another date?? ")
        if choice in affirm:
            continue
        else:
            break
def pythagorean():
    while True:
        speak("Enter a triad of numbers to determine if they are pythogorean or not")
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        c=int(input("Enter third number: "))
        if (a**2)==m.hypot(b,c):
            sub("The numbers are pythogorean triplets.")
        elif (b**2)==m.hyp(a,c):
            sub("The numbers are pythogorean triplets.")
        elif (c**2)==m.hyp(a,b):
            sub("The numbers are pythogorean triplets.")
        else:
            sub(f"The given numbers {a,b,c} are not pythogorean triplets.")
        choice=input("Do you want to check for another triplet?? ")
        if choice in affirm:
            continue
        else:
            break
def trigonometry():
    while True:
        speak("Enter value of angle in degrees or radians")
        aa=input("Is input in [D]egrees or [R]adians? ")
        if aa=="D" or aa=="d":
            l=[((180)/2)*i for i in range(1,1000)]
            val=float(input("Enter the angle in Degrees: "))
            val1=m.radians(val)
            speak("enabling trignometric calculator")
            term=int(input("What do you want to calculate?\n1)Sine\n2)Cosine\n3)Tangent\n4)Cosecant\n5)Secant\n6)Cotangent\nEnter the number: "))
            if val1 in l:
                a=1
            if term ==1:
                sub(f"The sine of given angle {val} degrees is: {m.sin(val1)}")
            if term ==2:
                sub(f"The cosine of given angle {val1} degrees is: {m.cos(val1)}")
            if term ==3:
                if a==1:
                    sub(f"Tangent of given angle {val1} degrees is not defined.")
                else:
                    sub(f"The tangent of given angle {val1} degrees is: {m.tan(val1)}")
            if term ==4:
                sub(f"The cosecant of given angle {val1} degrees is: {(1/m.sin(val1))}")
            if term ==5:
                if a==1:
                    sub(f"Secant of given angle {val1} degrees is not defined.")
                else:
                    sub(f"The secant of given angle {val1} degrees is: {(1/m.cos(val1))}")
            if term ==6:
                if a==1:
                    sub(f"The cotangent of given angle {val1} degrees is: 0")
                else:
                    sub(f"The cotangent of given angle {val1} degrees is: {(1/m.tan(val1))}")
        elif aa=="R" or aa=="r":
            val1=float(input("Enter the angle in Radians: "))
            l=[((m.pi)/2)*i for i in range(1,1000)]
            speak("enabling trignometric calculator")
            term=int(input("What do you want to calculate?\n1)Sine\n2)Cosine\n3)Tangent\n4)Cosecant\n5)Secant\n6)Cotangent\nEnter the number: "))
            if val1 in l:
                a=1
            if term ==1:
                sub(f"The sine of given angle {val1} radians is: {m.sin(val1)}")
            if term ==2:
                sub(f"The cosine of given angle {val1} radians is: {m.cos(val1)}")
            if term ==3:
                if a==1:
                    sub(f"Tangent of given angle {val1} radians is not defined.")
                else:
                    sub("The tangent of given angle {val1} radians is: {m.tan(val1)}")
            if term ==4:
                sub("The cosecant of given angle {val1} radians is: {(1/m.sin(val1))}")
            if term ==5:
                if a==1:
                    sub(f"Secant of given angle {val1} radians is not defined.")
                else:
                    sub("The secant of given angle {val1} radians is: {(1/m.cos(val1))}")
            if term ==6:
                if a==1:
                    sub(f"The cotangent of given angle {val1} radians is: 0")
                else:
                    sub(f"The cotangent of given angle {val1} radians is: {(1/m.tan(val1))}")
        choice=input("Do you want to calculate more trigonmetric equations?? ")
        if choice in affirm:
            continue
        else:
            break
def log():
    while True:
        speak("Enter a number to calculate the logarithimic value")
        b=input("Enter base of logarithm\n[Enter 1 for natural log] ")
        a=int(input("Enter the number whose log is to be calculated: "))
        if b=="1":
            sub(f"The natural log of {a} is {m.log(a)}")
        else:
            b=int(b)
            if b==2:
                sub(f"The log of {a} to the base {b} is {m.log2(a)}")
            elif b==10:
                sub(f"The log of {a} to the base {b} is {m.log10(a)}")
            else:
                sub(f"The log of {a} to the base {b} is {m.log(a,b)}")
        choice=input("Do you want to calculate more logarithims?? ")
        if choice in affirm:
            continue
        else:
            break
def greatestcommondivisor():
    while True:
        speak("To find the greatest common divisor")
        l=[]
        count=0
        n=int(input("Enter number of 'numbers' whose GCD is to be calculated: "))
        for i in range (0,n):
            if count==0:
                a=int(input("Enter 1st number: "))
                count+=1
            else:
                a=int(input("Enter next number: "))
            l.append(a)
        def findgcd(a,b):
            while b:
                a,b=b,a%b
            return a
        n1=l[0]
        n2=l[1]
        gcd=findgcd(n1,n2)
        for i in range (2,len(l)):
            gcd=findgcd(gcd,l[i])
        sub(f"\nThe Greatest Common Divisor of {l} is {gcd}")
        choice=input("Do you want to calculate more GCDs?? ")
        if choice in affirm:
            continue
        else:
            break
def root():
    while True:
        n=int(input("Which number's root do you want to calculate? "))
        sub(f"The square root of {n} is {m.sqrt(n)}")
        choice=input("Do you want to calculate more square roots?? ")
        if choice in affirm:
            continue
        else:
            break
def primefactors():
    while True:
        l=[]
        def primefactor(n):
            while n%2==0:
                l.append(2)
                n=n/2
            for i in range(3,int(m.sqrt(n))+1,2):
                while n%i==0:
                    l.append(i)
                    n=n/i
            if n>2:
                l.append(n)
        n=int(input("Enter number whose prime factors are required: "))
        primefactor(n)
        sub(f"The prime factors of {n} are: {l}")
        choice=input("Do you want to perform more prime factorizations?? ")
        if choice in affirm:
            continue
        else:
            break
def isprime():
    speak("Enter a number below to check whether it is prime or not")
    num =int(input("Enter a number: "))
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                sub(num, "is not a prime number")
                break
        else:
            sub(num, "is a prime number")
    else:
        sub(num, "is not a prime number")
def ispalindrome():
    speak("Enter a string below to check whether is a plaindrome or not")
    string=input("Enter a string: ")
    if string==(string[::-1]):
        sub(string,"is a palindrome.")
    else:
        sub(string,"is not a palindrome.")
def armstrong():
    speak("Do you want to check whether a number is an Armstrong number or not?")
    a=int(input("Enter a number: "))
    def power(a,b):
        return a**b
    def order(a):
        n=0
        while a!=0:
           n+=1
           a=a//10
        return n
    def isarmstrong(a):
        speak(f"To check whether {a} is an armstrong number or not")
        n=order(a)
        temp=a
        sum1=0
        while temp!=0:
            r=temp%10
            sum1+=power(r,n)
            temp=temp//10
        return (sum1==a)
    if isarmstrong(a):
        speak(f"{a} is an armstrong number.")
    else:
        speak(f"{a} is not an armstrong number.")
def strongnum():
    n=int(input("Please Enter any Number: "))
    Sum=0
    Temp=n
    while Temp>0:
        Factorial = 1
        i = 1
        Reminder=Temp%10
        while i<=Reminder:
            Factorial=Factorial*i
            i=i+1
        sub(f"Factorial of {Reminder} = {Factorial}")
        Sum+=Factorial
        Temp=Temp//10
    sub(f"Sum of Factorials of a Given Number {n} = {Sum}")
    if Sum==n:
        sub(f"{n} is a Strong Number")
    else:
        sub(f"{n} is not a Strong Number")  
def perfectnum():
    speak("Enter a number below")
    num = int(input("Please Enter any Number: "))
    Sum = 0
    for i in range(1,num):
        if num%i==0:
            Sum=Sum+i
    if Sum==num:
        sub(f"{num} is a Perfect Number")
    else:
        sub(f"{num} is not a Perfect Number")
def asciinum():
    a=input("Enter the charecter whose ASCII value is desired: ")
    sub(f"The ASCII (American Standard Code for Information Interchange) vaue of {a} is {ord(a)}")
def numthatarenotdivisble():
    l=[]
    speak('Enter lower limit of range below')
    start=int(input("Lower limit of range: "))
    speak('Enter upper limit of range below')
    end=int(input("Upper limit of range: "))
    a=int(input("Number shouldn't be divisible by(1): "))
    b=int(input("Number shouldn't be divisible by (2): "))
    speak(f"These numbers are between {start} and {end} and aren't divisible by {a} or {b}")
    for i in range(start,end+1):
        if(i%a!=0 & i%b!=0):
            l.append(i)
    sub(f"LIST ( {len(l)} numbers ): ")
    for i in l:
        print(i)
def profitloss():   
    speak("Please Enter the Actual Product Price below")
    actual_cost = float(input("Please Enter the Actual Product Price: "))
    speak("Please Enter the Sales Amount below")
    sale_amount = float(input("Please Enter the Sales Amount: "))
    if(actual_cost > sale_amount):
        amount = actual_cost - sale_amount
        sub("Total Loss Amount = {0}".format(amount))
    elif(sale_amount > actual_cost):
        amount = sale_amount - actual_cost
        sub("Total Profit Amount = {0}".format(amount))
    else:
        sub("No Profit No Loss!!!")
def romannumerals():
    digitval = (1000,500,100,50,10,5,1)
    digit = ("M","D","C","L","X","V","I")
    arabic = abs(int(input("Enter a whole number: ")))
    roman = ""
    sub(f"In Roman numerals, {arabic} is represented by:")
    for n in range(7):
        while arabic>=digitval[n]:
              roman=roman+digit[n]
              arabic=arabic-digitval[n]
        if n < 6:
            if arabic >= digitval[n] - digitval[n+1+((n+1) % 2)]:
                roman = roman + digit[n+1+((n+1) % 2)] + digit[n]
                arabic = arabic - (digitval[n] - digitval[n+1+((n+1) % 2)])
    print(roman)
def studentgrade():
    speak("Enter number of subjects below")
    n = int(input("Number of subjects: "))
    print("[Subject Name] {space} [Marks]")
    d = dict((input("Enter: ")).split() for _ in range(n))
    total=0
    for i in d:
        total+=int(d[i])
    percentage=(total/(n*100))*100
    sub(f"Total marks is: {total}/{n*100}")
    sub(f"Your percentage is: {percentage}")
    if(percentage >= 90):
        grade=("A Grade")
    elif(percentage >= 80):
        grade("B Grade")
    elif(percentage >= 70):
        grade=("C Grade")
    elif(percentage >= 60):
        grade=("D Grade")
    elif(percentage >= 40):
        grade=("E Grade")
    else:
        grade=("F grade")
    sub(f"You have received overall grade as: {grade}")