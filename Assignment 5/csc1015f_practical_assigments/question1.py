def gcd():
    a=eval(input("Enter the numerator:\n"))
    b=eval(input("Enter the denominator:\n"))
    
    m=a
    n=b
    
    while n!=0:
        m,n=n,m%n
    print("Simplified fraction:"," ",a//m,"/",b//m,sep="" )
    
gcd()