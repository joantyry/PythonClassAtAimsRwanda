'''
Write a short formula that computes the length sideC of the hypotenuse of a right triangle given two
sides sideA = 6 and sideB = 8. Print the length of sideC on the screen.
'''
import math
def ComputeHypotenuse(A = 6, B = 8 ):
	C = math.sqrt(A**2 + B**2)
	return C

if __name__ =="__main__":
	print (ComputeHypotenuse())
	
