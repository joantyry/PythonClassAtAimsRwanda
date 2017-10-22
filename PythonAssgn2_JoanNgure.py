# -*- coding: utf-8 -*-
"""
Name: 	  Joan Watiri Ngure
Subject : Assignment 2 and correction of assignment one 

I used python 2 to solve the problems.

"""

from math import*
import cmath
import random
import numpy as np
from matplotlib import pylab
import pylab as pl



def CelciusToFahrenheit():
	"""
	Note1 Q4
	This program converts temperature given in degree Celcius to Fahrenheit using a given formular.
	Tf = Tc ∗ 1.8 + 32.
	"""
	Tc =input("Input your temparature in degrees celcius:")
	Tf = float(Tc * 1.8 + 32)
	print("Converting %g degrees Celsius into degrees Fahrenheit gives %g" %(Tc, Tf))




def CalLength(A= 6, B = 8):
	"""
	Note1 Q5
	This program calculates the length of C which is the hypotenuse given two sides A and B.
	"""
	C = sqrt(A**2 + B**2)  
	print ("The hypotenuse C = ",C)



def totalamount(y=30, s=10000, i=8):
	""" 
	Note1 Q7
	This program calculates the total amount of savings given y as the number of years the person wishes to save before retirement,
 	s as the amount the person saves in three months and i as the annual interest rates.    
	"""
	AnnualSavings = (12*s)/3 #This converts the amount of savings in three months to annual savings
	TotalAmount = AnnualSavings * (100+ i)/100 * y #calculates the total amount after 30years including the annual interest
	print ("After 30 years your total savings = ", TotalAmount)


def Evaluator(a = 2.75,b= 1,c = pi/2,y=2,t=1):
	"""
	Note1 Q8
	This program evaluates the following: a) f(x)= 1/(1 + x^2)  if x = 2.75, b) u(x) = xIn(x + 2x − 1)  if x = 1, 
	c)v(x) = (1+sin(2x))/x  if x = pi/2,  d) w(t, y) = ty/(t + y) if t = 1 and y = 2

	"""
	f = 1/(1+a**2)
       
	u = b*log(b**2 + 2*b - 1)
        
	v =(1+sin(2*c))/c
    
	w=(t*y)/(t+y)
        
	print("f(%g) = %.5f, u(%g) = %.5f, v(%g) = %.5f, and w(%g,%g) = %.5f" %(a,f,b,u,c,v,y,t,w))        
        

def Newtons(T0 = 100,A = 60,k = 0.0367):
	"""
	Note1 Q9
	This program evaluates Newtons law of cooling that states when an object with an initial temperature T0 is placed in a
	environment with temperature A, it reaches a temperature T (t) at time t minutes later given by
	T(t) = (T0 − A)e −kt + A ,assuming that T0 = 100, A = 60degreeC and k = 0.0367. It evaluates when t = 5,10,15 and 20.
	"""
	T5 = (T0 - A)*exp(-k*5) + A 
	T10 = (T0 - A)*exp(-k*10) + A 
	T15 = (T0 - A)*exp(-k*15) + A   
	T20 = (T0 - A)*exp(-k*20) + A 
	print("T5=%f,T10=%f,T15=%f,T20=%f"%(T5,T10,T15,T20))


def RetirementSavings(y=30,i=8):
	"""
	Note1 Q10
	A young researcher wishes to save for his retirement in 30 years(y) time. He decides to invest into a saving
	account paying 8% annual interest(i).He save a regular amount every month.This program asks
	how much the researcher is willing to save monthly and prints out how much will be saved when he
	retires
	"""
	MonthlySavings = input("Please enter the amount you want to save monthly ") 
	Totalamount= MonthlySavings*12*((100+i)/100)*y
        
	print("Your retirement amount will be ", Totalamount)

def Numbers():
	"""
	Note2 Q3
	This program asks the user to enter two numbers, and prints their sum, their difference and
	their average, first each on a single line and then all in the same line.
	"""
	r = input("Enter your first number ")
	p = input("Enter your second number ")
	w = p + r
	print (w)
	v = abs(p-r)
	print(v)
	x = (p+r)/2
	print(x)
	print("sum=%f,difference=%f,average=%f"%(w,v,x))

def Times():
	"""
	Note2 Q4
	This program prompts the user to enter and integer n and outputs the letter ’x’, n times on a
	single line, without space.
	"""
	n = input("Enter the number of times you want to print out x ")
	print ('x'*n)

def Largest():
	"""
	Note2 Q5
	This program asks the user two numbers, and prints the largest
	"""
	h = input("Enter your first integer ")
	k = input("Enter your second integer ")
	if h > k :
		print("Your first integer is largest",h)
	elif h<k:
		print("Your second integer is largest",k)
	else:
		print("Your integers are equal",k,h)
	

def Value():
	"""
	Note2 Q6
	This program asks the user for 2 numbers x and y and returns the value of
	f(x,y) = ((x+y)/(1+y**2), 1/(1+x**2), xyexp(-2x))
	"""
	x = input("Enter the value of x ")
	y = input("Enter the value of y ")
	f =  ((x+y)/(1+y**2), 1/(1+x**2), x*y*exp(-2*x))
	print("f(x,y) = ((x+y)/(1+y**2), 1/(1+x**2), xyexp(-2x)) = ", f)

def LeapYear(i = 4):
	"""
	Note2 Q17
	This program asks the user to enter a four digit year, and prints out whether that year is a
	leap year or not. Hint: Look up ’leap year’ on Wikipedia for the definition of a leap year, and work
	from there.
	"""
	m = str(input("Enter your year "))
	
	if len(m)==4:	
		if int(m) % i == 0:
			print ("The year is leap")
		else:
			print ("The year is not leap")
	else:
		print ("Invalid input")

def Coefficient(a1=1,b1=1,c1=2,a2=2,b2=1,c2=2):#incase the user does not input the values.
    """
    Note2 Q18
    Write the program to find the coordinates of the intersection, if any,
    of the lines a1 x + b1 y = c1 and a2 x + b2 y = c2 .Write the program 
    to find the coordinates of the intersection, if any,
    of the lines a1 x + b1 y = c1 and a2 x + b2 y = c 2 .
    """
    a1,b1,c1 = input("Please enter the coef a1,b1,c1 each value separated by a comma of the first equation: ")
    print("a1=%d,b1=%d,c1=%d"%(a1,b1,c1))
	
   
    a2,b2,c2 =input("Please enter the coef a2,b2,c2 each value separated by a comma of the second equation: ")
    print("a2=%d,b2=%d,c2=%d"%(a2,b2,c2))
   
    det = a1*b2 - a2*b1   # the determinant of the system
    if det == 0:
        print("The two lines do not intersect")
    else:
        
        detx = b2*c1 - b1*c2 
        dety  = a1*c2 - a2*c1
        x = detx/det
        y = dety/det
        print("The co-ordinate of intersection is (%f, %f)."%(x,y))
        
def Large():
    """
    Note1 2
    Compute T = sum of all k, from k = 1 to K = n. Compute for n = 10, n = 20 and n = 100. 
    What happens when n gets larger and larger?
    Explain. Hint : Note that T is sum of terms of a geometric sequence.
    """   
    n =input("Enter an integer n : ")
    T=0  
    
    if int(n):
        for i in range(1,n):
            T += pow(2,i)
        print ("The sum is ", T)

    
    else:
                print ("Invalid input. Then number must be greater than zero")
                

def Abbas():
    """
    Note2 2
    What is the value of ”Abba was a Swedish band popular during the 80s”[0:4]?
    """
    W = "Abba was a Swedish band popular during the 80s."
    print (W[0:4])
    
    
def quo():
    """
    Note2 8
    Write a program that asks the user for two numbers. If the second number is not zero, print the
    quotient of the two numbers, otherwise print a message to the effect of not being able to divide by
    zero.
    """    
    k,l = input("Enter two numbers k,l separated by a comma ")
    if l == 0:
        print ("You cannot divide by zero.")
    else:
	a = k/l
        print("The quotient is ", a)    

	
def numbers():
    """
    Note2 9
    Write a program that asks the user to enter 0 or 1 or 2. If 1 is chosen, ask
    for a real number, raise it to the power of 5 and print the result with 10 decimal places. If 2 is chosen,
    ask for an integer n and return the parity (odd or even) of n. If 0 is chosen print ”I hate zero!”
    """	
    j = input("Choose a number between 0,1,2 ")
    if j == 0:
        print ("I hate zero!")
    elif j == 1:
        h = input("Enter a real number")
        t = pow(h,5)
        print ("%.10f" %t)
    elif j==2:
        k=input("Enter a number")
        if type(k) == int:
            if k%2 == 0:
                print ("The number is even")
            elif k%2 != 0:
                print("The number is odd")
            else:
                print ("Invalid input")
    else:  
            print("Invalid input") 
            
          
def smallest():
    """
    Note2 11
    Write a program that asks the user to enter 4 numbers, and prints the smallest
    """  
    u,i,o,p = input("Please input four numbers separated by commas ")
    if type(u)== int and type(i)== int and type(o)== int and type(p)== int :
        print ("Your minimum number is", min(u,i,o,p))  
        
def string():
    """
    Note2 13
    Write a program that given a string s, returns a string made of the first 2 and the last 2 characters
    of the original string, so ’spring’ yields ’spng’. However, if the string s is less that 5 characters long,
    returns s.
    """    
    s = raw_input("Please type anything ")
    if len(s) < 5:
        print (s)
    else:    
        k = s[0:2]
        h = s[-2:]
        
        print("Your first and last two characters are ",k + h)
        
def ing():
    """
    Note2 15
    Write a program that given a string, adds ’ing’ to its end if its length is at least 3 unless it already ends
    in ’ing’, in which case add ’ly’ instead. If the string length is less than 3, leave it unchanged. Return
    the resulting string.
    """  
    p =raw_input("Please type any word you think of ")  
    if len(p)> 3:
        if p[-3:] == "ing":
           print (p + "ly")
        else:
            print (p + "ing")
    else:
        print(p)   
        
        
def Quadratic():
    """
    Note2 16
    Write a python script that asks for 3 numbers a,b and c and solves the
    quadratic equation ax**2 + bx + c = 0. Print the answer with five decimal places.
    """    
    r,t,y = input("Please input three numbers separated by commas ")
    det = (t**2) - (4*r*y) #the determinant
    sol1 = (-t-cmath.sqrt(det))/(2*r)
    sol2 = (-t+cmath.sqrt(det))/(2*r)

    print('The solutions are {0} and {1}'.format(sol1,sol2))
    
def LargestOddDivisor():
    """
    Note3 4
    Write a program that takes an integer n and output the largest odd divisor of n
    """  
    n = int(input("Please input an integer ") )
    lis1 = [i for i in range(1, n+1) if n % i == 0]
    #print lis1
    lis2 =[]
    for num in lis1:
        if num % 2 != 0:
            lis2.append(num)
    print("Your largest odd divisor is", max(lis2) )
    
def intger():
    """
    Note3 15
    How many integers between 1 and 250, including 1 and 250, are divisible neither by 3 nor by 7 but are
    divisible by 5 
    """    
    lis = [n for n in range(1,251) if n%5==0 and n%3 != 0 and n%7 != 0]
    print ("The numbers divisible by 5 only are: ", len(lis))
    
def ordering():
    """
    Note3 16
    Write a program that
    (a) prompts the user to enter an integer n
    (b) prompts the user to enter n integers
    (c) prints out these n integers in ascending order
    """ 
    n = int(input("Please enter the number of integers you want to output "))  
    L = list()
    for i in range(1, n+1) :
        g = int(input("Please enter an integer %d :"%i)) 
        L.append(g)
        L.sort()
    print("You enter the following numbers in ascending order", L)
    
def grades():
    """
    Note3 17
    Students grades are given as a list of tuples each specifying a subject name and a grade symbol (’A’ -
    ’F’). A is the highest grade, B the next highest grade, etc. Here are the grades for a student named
    Georges:
    [(Maths, D), (Comp Sci, B), (English, C), (French, A),
    (Physics, B), (History, E), (Chemistry, A)].
    Write a program (see Grades.py) that:
    (a) prints out the subject(s) with the highest mark.
    (b) outputs each subject and the grade symbol in the format subject: grade, with each subject on a
    single line.
    (c) prints out a tab separated list of subjects on the first line, and the corresponding grades, also tab
    separated on the second line.
    """    
    Georges = {'Maths': 'D', 'Comp Sci': 'B', 'English': 'C', 
    'French': 'A', 'Physics': 'B', 'History': 'E', 'Chemistry': 'A'} 

    a = Georges.keys() 
    b = Georges.values()


   
    print ("You scored highest in :")
    for i in Georges:
        if Georges[i] == min(b):
            print (i)
    print ("\n")

    print ('{0:10s} {1:1s} {2:5s}'.format('Subjects', ':', 'Grades') )
    for i in Georges:
        print  ('{0:10s} {1:1s} {2:7s}'.format(i ,': ', Georges[i]))

    print ('\n')



    for i in Georges:
        print  (i + "\t   "  ),
    print ("")   		
    for i in Georges:
        print   (Georges[i]+"\t\t"),

def Counting(num):
	"""
	Note4 1pg5
	Write a program that generates 100000 random numbers between 0 and 1.
 	Count the number of occurrences where the number is less than or equal 
	to 0.5. Run the program several times and comment the ouputs
	"""

	c=0
	result = []
	result2 = []
	for i in range(num+1):
		rng = random.random()
		result.append(rng)
		if rng <= 0.5:
			c  += 1
	print (result)
	
	print ("Random numbers less than 0.5 = ",c)
		
def plotting():
	"""
	Note4 2pg7
	Plot the function f(x) = ln(x**2 + e**2x ) in the interval [−3, 3].
	"""
	x = pl.linspace(-3,3,100)
	y = pl.log(x**2 + pl.exp(2*x) )
	pl.plot(x,y)
	pl.title("Plot of f(x) = ln(x**2 + e**2*x ) ")
	pl.xlabel("x axis")
	pl.ylabel("y axis")
	#pl.xlim(-3, 3)
	#pl.ylim(0,10)
	pl.show()

def curve(t,v):
	"""
	Note4 8 pg17
	Make a program that reads a set of v0 values from the command line and plots the corresponding
	curves y(t) = v0t − 0.5gt**2 in the same figure (take g = 9.81). Let t ∈ [0, 2v/ g0 ] for each curve, which
	implies that you need a different vector of t coordinates for each curve.
	"""
	g =9.8
	return v*t-0.5*g*t**2
def curve2():
	n = int(input("How many times do you want to plot? "))
	w = []
	g = 9.8
	for i in range(1,n+1):
		v =input("Enter value of v %d : "%i)
		t = 2*v/g
		w.append((t,v))

	for t,v in w:
		pl.plot(curve(np.linspace(0, t, 100), v))
		pl.xlabel("time")
		pl.ylabel("y axis")
		pl.title("plot of v*t-0.5*g*t**2") 
		

	pl.show()

	
	

def guassian(x,x0,sigma):
	"""
	Note4 11pg8
	Let’s consider the formula of the normalized Gaussian distribution :
	f(x)= (1/((sigma) *sqrt(2*pl.pi)))* pl.exp((-(x-x0)**2)/2*(sigma**2))
	where x 0 is the mean value and σ the standard deviation. 
	Write a single script gaussian drawing.py
	• Plot on the same graphic three curves with different line styles to show the influence of x0
	• Plot on a second graphic three different curves to show the influence of σ
	All figures must have a title, labels on both axes and a legend
	"""
	return (1/((sigma) *sqrt(2*pl.pi)))* pl.exp((-(x-x0)**2)/2*(sigma**2))

	
def guassian2():
	#when x0 affects the graph
	n = int(input("How many times do you want to plot? "))
	s = []
	sigma = 3
	for i in range(1,n+1):
		x0 =input("Enter value of x0 %d : "%i)
		
		s.append(x0)

	for x0 in s:
		pl.plot(guassian(np.linspace(-10,10 , 100), sigma,x0))
		pl.title("Guassian Distribution")
		pl.xlabel('x0')
		pl.ylabel('y axis')
		

	pl.show()

def guassian3():
	#when sigma affects the graph
	n = int(input("How many times do you want to plot? "))
	s = []
	x0 = 3
	for i in range(1,n+1):
		sigma =input("Enter value of sigma %d : "%i)
		
		s.append(sigma)

	for sigma in s:
		pl.plot(guassian(np.linspace(-10,10 , 100), sigma,x0))
		pl.title("Guassian Distribution")
		pl.xlabel('sigma')
		pl.ylabel('y axis')
		

	pl.show()




if __name__ == "__main__":

    """
    This section executes the functions by calling them.
    
    """
	
    CelciusToFahrenheit()
    print (raw_input("press enter to continue "))	
    	
    CalLength()
    print (raw_input("press enter to continue "))
    
    totalamount()
    print (raw_input("press enter to continue "))
    
    Evaluator()
    print (raw_input("press enter to continue "))
    
    Newtons()
    print (raw_input("press enter to continue "))
    
    RetirementSavings()
    print (raw_input("press enter to continue "))
    
    Numbers()
    print (raw_input("press enter to continue "))
    
    Times()
    print (raw_input("press enter to continue "))
    
    Largest()
    print (raw_input("press enter to continue "))
    
    Value()
    print (raw_input("press enter to continue "))
    
    LeapYear()
    print (raw_input("press enter to continue "))
    
    Coefficient()
    print (raw_input("press enter to continue "))
    
    Large()
    print (raw_input("press enter to continue "))
    
    Abbas()
    print (raw_input("press enter to continue "))
    
    quo()
    print (raw_input("press enter to continue "))
    
    numbers()
    print (raw_input("press enter to continue "))
    
    smallest()
    print (raw_input("press enter to continue "))
    
    string()
    print (raw_input("press enter to continue "))
    
    ing()
    print (raw_input("press enter to continue "))
    
    LargestOddDivisor()
    print (raw_input("press enter to continue "))
    
    intger()
    print (raw_input("press enter to continue "))

    ordering()
    print (raw_input("press enter to continue "))

    grades()
    print (raw_input("press enter to continue "))

    Counting(100000)
    print (raw_input("press enter to continue "))

    plotting()
    print (raw_input("press enter to continue "))


    curve2()
    print (raw_input("press enter to continue "))

    guassian2()
    print (raw_input("press enter to continue "))

    guassian3()
