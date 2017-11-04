"""
Name : 	Joan Ngure
Version : Python2
Assigment3
"""

import random
import math
import numpy as np
from matplotlib import pylab
import pylab as plt
import csv
from operator import itemgetter
import collections
import Levenshtein
from sympy import diff,pprint,symbols
import scipy as sp
def Rand(length= 1000):
	"""
	Note4 1.4 q2
	Create a random DNA of length 1000 bases. DNAs are string on the alphabet a, c, g, t Write a computer
	program (gambling.py) that simulates a game between two players.The program must ask for each
	player to enter his name. Each player rolls a fair six-sided dice one after another. The process is
	repeated until a player gets a 6. The winner is the first player to get a 6. The program then returns
	the name of the winner.
	"""
	DNA_length= []
	i = ""
	for count in range(length):
		i+=random.choice("acgt")
	DNA_length.append(i)
	return DNA_length
	

def dice():
	throw = True
	Player1=raw_input("What is the name of player 1? ") 
	Player2 =raw_input("What is the name of player 2? ")

	p1 = 0
	p2 = 0
	
	while throw :
		w1= random.randint(1,6)
		w2= random.randint(1,6)
		p1 = w1
		print Player1,p1
		if p1 == 6:
			print Player1, 'is the winner.'
			break
		p2 = w2
		print Player2,p1
		if p2 == 6:
			print Player2, 'is the winner.'
			break
		
	
	
	
def guess():
	"""
	Note4 1.4 q3 
	Write a program (guessingNumber.py) that plays the game of guess the 
	number as follows: Your program chooses the number
	I have a number between 1 and 20.Can you guess my number?
	Please type your first guess
	The player then types a first guess. The program responds with one of the following :
	1. Exellent! You guessed the number!
	Would you like to try again (y or n)?
	2. Too low. Try again.
	3. Too high. Try again.
	If the players guess is incorrect, your program should loop until the player finally gets the number
	right. Your program should keep telling the player Too high or Too low to help the player zoom in on
	the correct answer. The program should stop after 10 unsuccessful attempts.
	"""	
	guess = random.randrange(1,20)
	attempts = 1
	
	p = int(raw_input("I have a number between 1 and 20. Please guess my number"))
	if p == guess:
		print 'Congratulations you got it'
			
	else:
		
		print 'Excellent, you guessed the number:',p
		a = raw_input ('Would you like to try again? y/n ')
	
	
		if a.lower() == 'y':
		
			
			
			while attempts < 10 :
				attempts +=1
				b = int(raw_input('Guess another number attempt %d : ' %attempts))
				if b < guess:
					print 'Too low.Try again'
				elif b > guess:
					print 'Too high.Try again'
				else:
					print 'Congratulations you got it'
			
						
			
			print 'You have exceeded your number of guesses. Thankyou for trying.'
			
		else:
			print'Thankyou for trying. Come back again later'

def monte():
	"""
	Note4 1.5 q2
	Count the number n of points
	p generated that fall inside the circle, that is those points M = (xi , yi )
	that satisfy CM <= r or sqrt((xi-r)**2+(yi-r)**2)<=r.
	"""
	count = 0
	r = 1
	points = input("Enter the number of points: ")
	
	x = [random.random() for a in range(points)]
	y = [random.random() for b in x]
	

	for xi, yi in zip(x,y) :
	  if (xi-r)**2+(yi-r)**2 <=r**2:
	    count += 1

	print "The points in a circle are", count

def circle():
	"""
	Note4 1.5 q3
	Show that the probability p that a point falls within the circle is given by
	Ac/As where Ac and As are the areas of the circle and the square respectively
	"""
	r = 1
	counter = 0.0 
	As = (2*r)**2
	Ac = math.pi*r**2
	p = Ac/As
	print 'The probability1(Ac/As) is ',p
	for y in range(1000):
		size_sample= np.random.uniform(0,2,100).reshape(2,int(100/2))
		a = size_sample[0]
		b = size_sample[1]	
		i =0.0
		for j in range(len(a)):
			if(a[j]-1)**2+(b[j]-1)**2<=1:
				i+=1
		counter+= i/len(a)
	pr = counter/1000
	
	print 'The probability2 is  ',pr
	print 'probability1 == probability2'


def basic():
	"""
	Note4 1.5 q4
	Lets pick N random points (x 1 , x 2 , . . . , x n ), 
	uniformly distributed in a multidimensional volume V .
	The basic theorem of Monte-Carlo integration estimate the integral of f over V by:
	"""
def plot1():
	"""
	Note4 1.6 q3
	Plot the function f(x) =(x**3 +x**2 - x+1)/(x-2)
	in the interval [0, 4]. Give a brief comment of your plot.
	"""
	x = np.arange(0,4)
	y =(x**3 +x**2 - x+1)/(x-2)
	plt.plot(x,y)
	plt.title('The plot of $y = (x^3 +x^2 - x+1)/(x-2)$' )
	plt.xlabel('x-axis')
	plt.ylabel('y-axis')
	plt.show()

def visulize(x,n):
	"""
	Note4 1.6 q5
	The sine function can be approximated by a polynomial according to the following formula:
	sin(x)=  S(x; n) =np.sum (-1)**j x**(2j+1)/(2j + 1)factorial
	The purpose of this exercise is to visualize the quality of various approximations S(x; n) as n increases.
	Write a Python function S(x; n) that computes S(x; n). Use a straightforward approach where you
	compute each term as it stands in the formula. Plot sin(x) on [0, 4pi] together with the approximations
	S(x; 1), S(x; 2), S(x; 3), S(x; 6), and S(x; 12).
	"""
	
	i=0
    	w = 0
    	while i <= n:
		w = w + (-1)**i*(x**(2*i + 1)/math.factorial(2*i + 1))
		i += 1
    	return w
	
def visulize2():
	
	
	h = [1,2,3,6,12]
	for num in h:
	
		plt.plot(visulize(np.linspace(0,4*math.pi),num))
		
		plt.title("Plot of $\sin(x) \sim S(x;%d)=\sum_{j=0}^{n}{(-1)^j x^{2j+1}/(2j + 1)!}$"%num)
		
		plt.xlabel('x axis')
		plt.ylabel('y axis')
		plt.show()

def formula(x,y0,v0,theta,g=9.81):
	"""
	Note4 1.6 10
	The formula below computes the height y = f (x) of a ball that is thrown with an initial velocity v0
	forming an angle theta with the horizontal.
	f(x) = xtan(theta) -(1/ 2*v0**2 )*(g*x**2/cos**2(theta))+ y0
	In this expression, x is a horizontal coordinate, g = 9.81 is the acceleration of gravity and (0, y0 ) is
	the initial position of the ball. (a) Write a program (see BallTrajectory.py) at first reads the input
	data y0 ,theta, and v0 from the command line. Then plot the trajectory y = f (x) for y >= 0.
	(b) Write a program (see BallTrajectorySimulation.py) that simulates the motion of the ball.
	Recall that at each time point t, the position of the ball relatively to the x,y-plane is given by
	"""
	
	return x*np.tan(theta) - (g*x**2)/( (2*v0**2)*(np.cos(theta))**2)+ y0
def formula2():
	
	y0 = int(raw_input("Please enter the initial position of the ball:  "))
	theta = int(raw_input("Please enter the angle in which you would want to project:  "))
	v0 = int(raw_input("Please enter the initial velocity of the ball:  "))
	print "Your initial position y0 is %d metres, angle theta is %d degrees and initial velocity is %d m/s"% (y0,theta,v0)
	if y0>= 0:
		d= plt.vectorize(formula)
		plt.plot( d(np.linspace(0,50 , 1000),y0,v0,theta))
		plt.title('Height')
		plt.xlabel('x')
		plt.ylabel('y')
		plt.show()

def guassian():
	"""
	Note4 1.6 13
	The 2-dimensional gaussian distribution is defined as follow :
	f(x,y) = A * np.exp(-((x-x0)**2/(2*sig_x**2))) * np.exp(-((y-y0)**2/(2*sig_y**2)))
	with A a multiplicative constant, x 0 and y 0 the mean values and sigma x and sigma y the standard deviations
	along x and y respectively. Create a function gaussian2d.py that allows to visualize a 2dimensional
	Gaussian distribution in the (x, y) plan for given values of A, x 0 , y 0 , sigma x and sigma y using imshow or
	contourf .
	Hint: you will need to first define a grid using meshgrid.
	"""
	sig_x,sig_y = input('Input your value of sigma_x and sigma_y separated by a comma')
	x0,y0,A = input('Input your value of x0,y0 and A separated by commas')
	
	x= np.linspace(-20,20,100)
	y = np.linspace(-20,20,100)
	x,y = np.meshgrid(x,y)
	equation = A * np.exp(-((x-x0)**2/(2*sig_x**2))) * np.exp(-((y-y0)**2/(2*sig_y**2)))
	plt.contourf(x,y,equation, cmap= 'pink')
	plt.colorbar()
	plt.show()
	

def m():
	"""
	Note4 2.3.1 10
	Create the following numpy array
	A = [[1,4,6],[0,-3,2],[-2,-2,-2]]
	B = [[2,-1,0], [2,-1,-0],[0,0,1]]
	Compute A-B, 4A + B, trace(A), tB the transpose of B, the determinant of A, AB and Bt A the
	matrix product of A and B.
	Create the numpy array v = [1, -1, 0]. Compute Av the matrix-vector multiplication.
	Find the eigenvalues and the eigenvectors of the matrix B. Hint. Use the linear algebra module
	in numpy.
	Solve the system Ax = v using the solve(A,v) function of linalg.
	perfom the QR factorization of A using the linalg function qr(A) (Check that Q is an orthogonal
	matrix, that is Q T Q = I).
	Perform the singular value decomposition of A using the linalg function svd(A)
	
	"""
	A = np.array([[1,4,6],[0,-3,2],[-2,-2,-2]])
	B = np.array([[2,2,2], [-1,-1,-3],[0,0,1]])
	
	print "A = \n", A 
	raw_input('press enter to get B, A-B,4A - B')
	print "B = \n", B
	print ''
	print ''
	print "The difference is \n", A-B
	print ''
	print ''
	print "4A - B =  \n", 4*A - B
	raw_input ('Press enter to get the trace of A,transpose of B,determinant of A ')
	print " Trace of A : ", sp.trace(A)
	print ''
	print ''
	print " Transpose of B : \n",sp.transpose(B)
	print ''
	print ''
	print "Determinant of A : ", np.linalg.det(A)
	raw_input('press enter to get AB, The matrix product of A and B,v')
	print "AB = \n",A*B
	print ''
	print ''
	print 'Matrix product of A and B : \n',sp.dot(A,B)
	print ''
	print ''
	v =np.array([1,-1,0])
	print 'v = ',v
	raw_input('press enter to get matrix-vector multiplication Av, eigen values,The eigen vectors')
	print 'Matrix-vector multiplication Av : \n', sp.dot(A,v)
	print ''
	print ''
	e_values, e_vectors = np.linalg.eig(B)
	print " Eigen values of B : ",e_values
	print " Eigen vectors of B : \n",e_vectors
	raw_input('press enter to get System solution, QR factorization,singular value decomposition')
	print "System solution Ax = v: \t", np.linalg.solve(A,v)
	print ''
	print ''
	print 'QR factorization: \n',np.linalg.qr(A)
	print ''
	print ''
	print 'Singular value decomposition of A: \n', np.linalg.svd(A)
def h():
	"""
	Note5 2
	Write a program (hat.py) that implements the hat function h defined as follows: 
	h=1 if x < 0, h=x if 0 <= x < 1, h=2-x if 1 <= x< 2, h=0 if x >= 2.
	"""
	for x in range(20):
		if  x < 0:
			print 1
		elif x >= 0 and  x < 1:
			print x
		elif x >= 1 and x< 2:
			print 2-x
		else:
			print 0

def prime():
	"""
	Note5 12
	Write a function that accepts a single integer parameter n, and 
	returns a list of the prime numbers less than n.
	"""
	n= int(raw_input("Enter a number n: "))
	prime_list = list()
	for num in range(2, n+1):
		if all(num % i != 0 for i in range(2, num)):
			prime_list.append(num)
    	
        	
	print prime_list
		
def derivative():
	"""
	Note5 16
	Write a function that takes a function f , a number x0 and 
	return the first two derivatives of f at x0
	"""
	func = raw_input('Provide your function to get the first and second derivatives with respect to x: ')
	#x0= input('Give your number to get the derivatives: ')
	r = symbols('x') 
	
	print 'The first derivative is: '
	pprint (diff(func,r,1))

	print 'The second derivative is: '
 	pprint(diff(func,r,2))
	

def menu():
	"""
	Note5 17
	A pizza restaurant proposes the following menu for its clients.
	Write a program (function)(pizza.py) that prompts the user to 
	choose an item from a menu list, then prompts the user to enter 
	the quantity of the required item and prints out the bill cost. 
	The function shall handle possible exception.
	"""
	menulist = {'Ugali': '100','Rice': '250','Matumbo': '300','Beef':'500'}
	#a = str(menulist.values())
	print '{0:10s} {1:1s} {2:5s}'.format('Food', '*', 'Price($)') 
	print '******************'
	for i in menulist:
		print  '{0:10s} {1:1s} {2:5s}'.format(i ,'*', menulist[i])
	
	
	choice = raw_input("Please select what you want to eat from the menu ")
	if choice.capitalize() in menulist.keys():
		print "Your choice is ",choice
		a = menulist.get(choice.capitalize())
		quantity =int(raw_input("Please enter the number of plates you want to be served "))
		print "Your bill is: $",int(a)*quantity
	else :
		print 'The diet is not available'
	
def trapezoid():
	"""
	Note5 18
	Write a (function) program that inputs an integer n and calculates the integral
	"""
	
	

	num = input('Please enter any integer: ')
	my_a=input("Provide a value for a= ")
	my_b=input("Provide a value for b= ")
	my_h = float(my_b-my_a)/num
	integral  = 0
	
	for k in range(1, num):
		x = my_a + k*my_h
		f = math.exp(x**2/2.)
		integral += f
	print 'The integral is: ',integral
	raw_input("Press enter")
	print(my_h)
	xn = my_a+ num*my_h
	fn = math.exp(x**2/2.)
	xo = my_a+ 0*my_h
	fo = 0.5*math.exp(x**2/2.)
	Integ = my_h *(fo+ integral + fn)
	print "The integral estimate: %0.10f with number = %d subdivisions" %(Integ,num)
	
	
def script():
	"""
	Note5 19
	Design a script that reads the file (UN-data.csv) load the data into a dictionary, write the subset of
	data where high low ='higher' into a file 'higher.txt' and the subset of data where high low = 'lower'
	in to the file 'lower.txt'. Use the dictionary to print the subset of the data where estimate less and
	equal to 50. In addition, it shall write into another reverse.txt in the reverse order.
	"""
	rows ={}
	f = 0
	UN = open("UN-data.csv","rU")#U opens it as universal
	reader =UN.read()
	reader2 = reader.split('\n')
	
	
        # csv.writer(load)
	for k in reader2:
		
		data = k.split(',')
		if k.startswith('prompt'):
			pass
		else:
			rows[f]= data[:]
		f+=1 
		#print k
	#print rows
	
	load_higher =  open("UN-dataHigher.csv", 'wt')
	load_lower =  open("UN-dataLower.csv", 'wt')
	load_reverse =  open("UN-dataReverse.csv", 'wt')

	for d in rows:

		if rows[d][1]== 'higher':
			
			load_higher.write("\t".join([str(p) for p in rows[d]])+"\n")
			
		elif rows[d][1]== 'lower':
			load_lower.write("\t".join([str(p) for p in rows[d]])+"\n")

		for w in rows:
			if int(rows[w][2]) <= 50:
			#for line in sorted(UN, key=lambda line: line.split()[2]):
				load_reverse.write("\t".join([str(p) for p in rows[w]])+"\n")

	load_higher.close()
	load_lower.close()
	load_reverse.close()
	
	
	reverse2 = open("UN-dataReverse.csv","rU").read()
	
	f ={}
	h = reverse2.split('\n')
	c = 0
	
	for i in h:
		a = i.split('\t')
		f[c]=a[:]
		c += 1
	print f


def dna():
	"""
	Note5 21
	The file dna.fas contains the following text
	> e.coli
	-cta-gagt
	> zebra fish
	cgctgctatgtacatgct-aat
	Write a program (dna.py) that reads the file, creates two lists, one containing the sequences names
	(e.coli and zebra fish) and the second containing the corresponding sequences. Compute the frequency
	of each of the charcters appearing in the e.coli sequence. Compute the Hamming distance between
	the two sequences, that is the number of non-gap positions where both sequences differ. E.g. Ham-
	ming(acttc, agt-a) = 2.
	"""
	sN = []
	cN = []
	Dna_file = open("dna.fas","r")
	
	for line in Dna_file:
		print line
	sequenceNames = 'e.coli', 'zebra fish'
	correspondingNames = 'acgtgtacctagc-cta-gagt','cgctgctatgtacatgct-aat'
	
	for a in sequenceNames:
		sN.append(a)
	print sN
	for b in correspondingNames:
		cN.append(b)
	print cN

	patterns =collections.Counter(cN[0])
	print patterns
	HammingDistance = Levenshtein.distance(cN[0], cN[1])
	print "The hamming distance is:", HammingDistance


def studentData():
	"""
	Note5 22
	Write a program (Ordering.py) that reads the file StudentList.txt and writes the content in another
	file in the following way : First column are the Students Numbers and second column are the Students
	Names order alphabetically.
	"""
	studentFile = open('StudentList.txt','r')
	studentFile = studentFile.readlines()

	studentFile2 = open('StudentListNew.txt','w',)
	ColumnNames =("Student_Number, Student_Name").split(',')
	print '\t'.join(ColumnNames)
	a = sorted(studentFile, key=lambda line: line.split()[1])

	for k in a:
		if k.startswith("Student"):
			pass
		else:
			studentFile2.write(k)
			print k
	
	studentFile2.close()


if __name__ =="__main__":
	print Rand()
	print(raw_input("Press enter to continue"))
	dice()
	print(raw_input("Press enter to continue"))
	guess()
	print(raw_input("Press enter to continue"))
	monte()
	print(raw_input("Press enter to continue"))
	circle()
	print(raw_input("Press enter to continue"))
	#basic()
	#print(raw_input("Press enter to continue"))
	plot1()
	print(raw_input("Press enter to continue"))
	visulize2()
	print(raw_input("Press enter to continue"))
	formula2()
	print(raw_input("Press enter to continue"))
	#guassian()
	print(raw_input("Press enter to continue"))
	m()
	#print(raw_input("Press enter to continue"))
	h()
	print(raw_input("Press enter to continue"))
	prime()
	print(raw_input("Press enter to continue"))
	derivative()
	print(raw_input("Press enter to continue"))
	menu()
	print(raw_input("Press enter to continue"))
	trapezoid()
	print(raw_input("Press enter to continue"))
	script()
	print(raw_input("Press enter to continue"))
	dna()
	print(raw_input("Press enter to continue"))
	studentData()
	
