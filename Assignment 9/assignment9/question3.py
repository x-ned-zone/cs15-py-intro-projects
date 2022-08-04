# program to solve easy Sudoku puzzles (where there is no ambiguity). 


# create an empty list
a=[]
s=[]

# prompt user for an in put and then create a 2D-array
for i in range(9):
    z=input()
    for j in range(9):
        a.append(int(z[j]))
    s.append(a)
    a=[]

# initiate increment to zero
increment= 0
# create an empty list

# go over the array 
while increment<1500:
    
    for i in range(9):
        for j in range(9):
            # if sudoku is not solved make a solution to fill the cells swith possible values
            if s[i][j]==0:
                row = s[i]
                col = []
                for index in range(9):
                    col.append(s[index][j]) 
              
                value = [s[x][y] for x in range(9) for y in range(9) if ((i//3)*3 <= x < (i//3)*3 +3) and ((j//3)*3 <= y <(j//3) * 3 +3)]
                # possess an array of possible values 
                possiblevalues = [ posi for posi in range(1,10) if(posi not in row) and (posi not in col) and (posi not in value)]
                # only fill in value if there is only one possibility       
                if len(possiblevalues)==1:
                    s[i][j]= possiblevalues[0] 
       # increment c by one for nine times                             
    increment+=1             
# again check the if the sudoku puzzle is solved or not if bot find an alternative solution to solve it ...
def solved(b):   
    try:         
        i  = s.index(0)   
    except ValueError:                  
        return s      
    c = [s[j] for j in range(81)      
         if not ((i-j)%9 * (i//9^j//9) * (i//27^j//27 | (i%9//3^j%9//3)))]   
    
    for v in range(1, 10):         
        if v not in c:           
            r = solve(s[:i]+[v]+s[i+1:])    
            if r is not None:             
                return r  

# display the output result after the input has been processed and solved... 
import copy  
def display (b):
    if A:         
        for i in range (9):             
            for j in range (9):                 
                if type (A[i][j]) == type ([]): 
                    print (A[i][j][0])
for Atempt in s:
    for solved in Atempt:
        print(solved,end='')
    print()