#

def triangle():
    a=eval(input("Enter the height of the triangle:\n"))
    for i in range (a):
        print(" "* i,"*"*(a-i),sep="")
triangle()