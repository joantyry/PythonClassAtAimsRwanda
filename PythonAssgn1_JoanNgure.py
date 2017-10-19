# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from math import*
def CelciusToFahrenheit():
	"""
	Note1 Q4
	This program converts temperature given in degree Celcius to Fahrenheit using a given formular.
	Tf = Tc ∗ 1.8 + 32.
	"""
	Tc =eval(input("Input your temparature in degrees celcius:"))# The user is prompted to enter the temperature they want to convert.
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
	MonthlySavings = eval(input("Please enter the amount you want to save monthly ")) 
	Totalamount= MonthlySavings*12*((100+i)/100)*y
        
	print("Your retirement amount will be ", Totalamount)

def Numbers():
	"""
	Note2 Q3
	This program asks the user to enter two numbers, and prints their sum, their difference and
	their average, first each on a single line and then all in the same line.
	"""
	r = eval(input("Enter your first number "))
	p = eval(input("Enter your second number "))
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
	n = eval(input("Enter the number of times you want to print out x "))
	print ('x'*n)

def Largest():
	"""
	Note2 Q5
	This program asks the user two numbers, and prints the largest
	"""
	h = eval(input("Enter your first integer "))
	k = eval(input("Enter your second integer "))
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
	x = eval(input("Enter the value of x "))
	y = eval(input("Enter the value of y "))
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
    a1,b1,c1 = eval(input("Please enter the coef a1,b1,c1 each value separated by a comma of the first equation: "))
    print("a1=%d,b1=%d,c1=%d"%(a1,b1,c1))
	
   
    a2,b2,c2 =eval(input("Please enter the coef a2,b2,c2 each value separated by a comma of the second equation: "))
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

if __name__ == "__main__":

    """
    This section executes the functions by calling them.
    
    """
	
    CelciusToFahrenheit()
    print (input("press enter to continue "))	
    	
    CalLength()
    print (input("press enter to continue "))
    
    totalamount()
    print (input("press enter to continue "))
    
    Evaluator()
    print (input("press enter to continue "))
    
    Newtons()
    print (input("press enter to continue "))
    
    RetirementSavings()
    print (input("press enter to continue "))
    
    Numbers()
    print (input("press enter to continue "))
    
    Times()
    print (input("press enter to continue "))
    
    Largest()
    print (input("press enter to continue "))
    
    Value()
    print (input("press enter to continue "))
    
    LeapYear()
    print (input("press enter to continue "))
    
    Coefficient()
