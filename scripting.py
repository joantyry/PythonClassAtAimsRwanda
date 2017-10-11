"""
 This is our first scripting class.
What is a good structure of a python program
1. Description
2. Importations- import all the libraries you want to use.
3. Body of the program
To use the function you have to call it.
4. The execution part eg
	if __name__ == "__main__":
		    y= math.sin(45)
		    print(y)
"""
"""
Write a program called greetings.py that prompts the user to enter is name and returns Hello
followed the name entered
"""
d = input("What is your name?")
d = d.capitalize()
print ("Hello"+ " ", d)

#FUNCTIONS
import math as mt
def my_power(x,y):
	z= y**x
	return z
def my_test(a,b):
	u = a**b
	r = mt.exp((a+b**2)/a)
	return u,r
if __name__ == "__main__":
	w = my_power(2,4)
	print(w)
	h,j = my_test(3,4)
	print (h,j)
