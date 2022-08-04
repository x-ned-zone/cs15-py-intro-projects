# program to do basic vector calculations in 3 dimensions: addition, dot product and normalization

# ask for an input from the user twice
q=input("Enter vector A:\n")
A=q.split(" ")
v=input("Enter vector B:\n")
B=v.split(" ")

# create an array to store the calculated vetor additioh
vect1=[]
# calcute the vector addition
x=int(A[0])+int(B[0])
vect1.append(x)
# calcute the vector addition
y=int(A[1])+int(B[1])
vect1.append(y)
# calcute the vector addition
z=int(A[2])+int(B[2])
vect1.append(z)
# diplay the output
print("A+B","=",vect1)
# calculate the dot product of the same vector 
dot=int(A[0])*int(B[0])+int(A[1])*int(B[1])+int(A[2])*int(B[2])
# diplay the output
print("A.B","=",dot)

from math import sqrt
# calculating the norm of the vector
normA=sqrt(int(A[0])**2+int(A[1])**2+int(A[2])**2)
print("|A|","=","{0:.2f}".format(normA))
normB=sqrt(int(B[0])**2+int(B[1])**2+int(B[2])**2)
print("|B|","=","{0:.2f}".format(normB))