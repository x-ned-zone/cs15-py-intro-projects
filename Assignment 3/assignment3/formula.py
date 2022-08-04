#


def formula():
    a,b,c=eval(input("Enter 3 numbers:\n"))
    if a+b==c:
        print("The formula is:",max(a,b),"+",min(a,b),"=",c,"")
    elif a+c==b:
        print("The formula is:",max(a,c),"+",min(a,c),"=",b,"")
    elif b+a==c:
        print("The formula is:",max(b,a),"+",min(b,a),"=",c,"")
    elif b+c==a:
        print("The formula is:",max(b,c),"+",min(b,c),"=",a,"")
    elif c+a==b:
        print("The formula is:",max(c,a),"+",min(c,a),"=",b,"")
    elif c+b==a:
        print("The formula is:",max(c,b),"+",min(c,b),"=",a,"")
        
    else:
        print("There is no valid formula.")

        
formula()