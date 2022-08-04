# program to check if a complete Sudoku grid is valid or not.

# creating empty list/arrays for storage of numbers in a 2D-array
a=[]
b=[]

# loop over the sudoku grid to promp for an input

for i in range(9):
    z=input()
    for j in range(9):
        a.append(int(z[j]))
    b.append(a)
    a=[]
# initialising to zeroes to sum the numbers in the colum ,row and grid 
z=0
t=0
sum=0
w=0
# itetrate over the first grid to check if the sum of the numbers of this grid is 45
for k in range(3):
    for col in range(3):
        sum+=(b[k][col])
    if sum==45:
        pass
# also iterate over the first column to check if the sum is 45
for j in range(9):
    z+=(b[j][0])
    if z==45:
        pass
# also iterate over the first row to check if the sum is 45
for p in range(9):
    t+=(b[0][p])
    if t==45:
        pass
# also iterate over the last bottom row to check if the sum of the numbers is 45
for f in range(9):
    w+=(b[8][f])
    if w==45:
        pass
# create a boolean structure such that as the conditions are met the statement below be print 
if sum==45 and z==45 and t==45 and w==45:
    print("Sudoku grid is valid")
# else the conditions or one of the conditios are not met this should be printed
else: 
    print("Sudoku grid is not valid") 
