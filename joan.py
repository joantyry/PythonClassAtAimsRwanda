#This is our first lesson
# Python is case sensitive
x = 8*7
y = (8*7)/3
print(x)
print(y)

z = x - y
print("The value of z is" +" ",z)

# we use multiple commands separated by a semicolon
p = 20; w =30; c = p+w
print(c)

#1. Numbers: intergers(int), float(float), complex, +, -,*,%,**

#Complex
k = 2
p = complex(k)
print(p)

#integer
t= 7.8
w = int(t)
print (w)
A = w/x #gives float in python3 
#A = w//x #gives integer
print(A)
#c = 2+ 6j
#print (float(c))

#2. STRINGS
q = 'Joan'
s = 'Irene'
u = 'Mwasi'
# to put several lines
b = """are friends to Jacky. They spend time together.
They are intelligent, brilliant and neat. """
f = q + ',' +s +','+ u +" "+ b
print(f)
#All integers can be strings but all strings cannot be numbers

F = f.count('a') #counts the number of occurence of the alphabet a
print (F)

B = "My name is Joan"
B = B.split(" ")# This is what separates the words.
print(B)
#b. then press tab checks the operations you can perform on that variable

#3.BOOLEANS = true or false
# and, or, ==, <=, >=

e= True
E = False 
Ee = e and E
print (Ee)

#4.DERIVED OBJ : list,set,tuple,dict

#Basic Math Module
# A function is a well defined relationship with an expected output
import math 
l = math.sin(90)
print(l)

#you can import math as a shortcut
import math as kl
w = kl.cos(90)
print (w)

#To check what a funtion does '?math.sin' to any function.

#Another way to import math
from math import sin,cos,exp
r = cos(45)
print(r)

#To load all the functions in that library(math).
from math import *
k = cos(30)
print(k)

