# Python program with a recursive function to calculate the GCD (greatest common divisor) of 2 integers.

# prompt the user for an input 
Numbers=input("Enter two numbers:\n")
# split the numbers with empty space
N=Numbers.split(" ")
# now assign the following variables to the corresponding positions in the list/array  
x=int(N[0])
y=int(N[1])

# define the gcd function with two parameters
def gcd(x, y):
 # return the calculation of gcd
 return gcd(y, x % y) if y else abs(x)
# then display the output...after calling the function with the two parameters from the user's input
print("The GCD is:",gcd(x,y ))
