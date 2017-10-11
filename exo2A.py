'''
The program computes the sum of a geometric sequence in a given range.
'''

import math

def f(n):
	T=0
	for i in range(n):
		T += math.pow(2,i+1)
	return T
if __name__=="__main__":
	x = input("Enter n :")
	x=int(x)
	print(f(x))

'''
What happens when n gets larger and larger? The larger the value of n the larger the output 
but it reaches a point where an error is returned since there is insufficient memory
'''
