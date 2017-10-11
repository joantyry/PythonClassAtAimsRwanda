"""
This program converts temperature given in degree Celcius to Fahrenheit using a given formular.
Tf =
Tc ∗ 1.8 + 32.
"""
def CelciusToFahrenheit(Tc):
	Tf = Tc * 1.8 + 32
	return Tf

if __name__ == "__main__":
	Tc = input("Input your temparature in degrees celcius:") 
	TC = int(Tc)
	print (CelciusToFahrenheit(Tc))		

