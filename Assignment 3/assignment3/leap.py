# Leap year

import math
def leap():
    n=eval(input("Enter a year:\n"))
    
    if n%400==0 or (n%4==0 and not n%100==0):
        print(n,"is a leap year.")
    else :
        print(n,"is not a leap year.")

leap()