# A Python module for a simple Gumatj arithmetic
# Masixole Ntshinga
# 16 April 2012

def gumatj_to_decimal(num):
    if num>4:
        x=num//10
        y=x*5
        z=num%10
        return (z+y)
    else:
        return num

def decimal_to_gumatj(num):
    
    if num>4:
        x=num//5
        y=x*10
        z=num%5
        return (y+z)
    else:
        return num

def gumatj_add(num1, num2):
    k=num1 + num2
    n=k//10
    z=k%10
    v=z//5
    w=z%5
    p=v*10
    return (n*10+w+p)
        
def gumatj_multiply(num1, num2):
    p=num1*num2
    num1=p//5
    num2=num1*10
    z=p%5
    return(z+num2)