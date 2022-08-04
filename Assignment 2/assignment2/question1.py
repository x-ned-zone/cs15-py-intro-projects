import math

a=2/(math.sqrt(2+math.sqrt(2+math.sqrt(2))))
b=2/(math.sqrt(2+math.sqrt(2)))
c=2/(math.sqrt(2))
f=2
pi=(a*b*c*f)
print("Approximation of pi:",round(pi,11))

def radius():
    x=eval(input("Enter the radius:" "\n"))
    print("Area:",x*x*pi,)
radius()
    
