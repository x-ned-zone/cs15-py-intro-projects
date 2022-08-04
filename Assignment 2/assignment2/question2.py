# A program to sort three numbers entered by the user in ascending order using only math functions like min and max.
# by : Masixole Ntshinga
# 05 March 2012



import math
def main():
    
    a=eval(input("Enter number 1:" "\n"))
    b=eval(input("Enter number 2:" "\n"))
    c=eval(input("Enter number 3:" "\n"))
    x=min(a,b,c)
    y=max(a,b,c)
    z=(a+b+c)-(x+y)
    print("The sorted numbers are:",x,z,y)
    
main()
