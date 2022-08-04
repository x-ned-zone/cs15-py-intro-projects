a=eval(input("Enter the starting point N:\n"))
b=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

from math import sqrt
for i in range(a+1,b):
    is_prime = True
    for j in range(2,int(sqrt(i)+1)):
        if i%j==0:
            is_prime = False
            break
    if is_prime == True:
        x=(str(i)[::-1])
        x=int(x)
        if x==i:
            print(x)
        
           
        
        
            

