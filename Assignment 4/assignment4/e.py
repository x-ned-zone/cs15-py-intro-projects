
from math import factorial
def main():
    a=0
    b=0
    t=0
    while a<16 :
        t=1/factorial(a)
        b=b+t
        a=a+1
    print(round(b,11))
main()        
    