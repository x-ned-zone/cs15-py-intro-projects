# A program that takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks according to the mark categories at UCT
# Masixole Ntshinga
# 15 March 2012


list_of_marks=input("Enter a space-separated list of marks:\n")
m=list_of_marks.split(" ")

count=[0,0,0,0,0]

for i in m:
    int_z=int(i)
    
    if int_z<50:
        count[0]+=1
    elif 50<=int_z<60:
        count[1]+=1
    elif 60<=int_z<70:
        count[2]+=1
    elif 70<=int_z<75:
        count[3]+=1
    elif int_z>=75:
        count[4]+=1
        
print("1 |","X"*count[4],sep="")
print("2+|","X"*count[3],sep="")
print("2-|","X"*count[2],sep="")
print("3 |","X"*count[1],sep="")
print("F |","X"*count[0],sep="")
