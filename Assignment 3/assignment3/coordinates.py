#

import math
def coordinates():
    h,m,s,H,M,S=eval(input("Enter 6 numbers:\n"))
    if -90<=h<=90 and 0<=m<=59 and 0<=s<=59 and -180<=H<=180 and 0<=M<=59 and 0<=S<=59:
        print("WOW! Looks like geographic coordinates!")
    else:
        print("Hmmm ... looks like 6 random numbers.")
        
coordinates()