# Python program to analyse student marks read in from a file and determine which students need to see a student advisor
# Masixole Ntshinga
# 30 April 2012
import sys 
from math import sqrt 
# open the file with data
filename=input("Enter the marks filename:\n")
f=open(filename, "r")

x=[]
for line in f.readlines(): 
   y = [value for value in line.replace("\n","").split(",")]
   x.append(y)
   
   
# initialsing the counters to zero to add the marks and eventually divide by their number
total=0
st=0
for i in range(len(x)):
   total= total + (int(x[i][1]))
# divide by their number
ave = total/len(x)
# display the output as calculated in the code
print("The average is:","{0:.2f}".format(ave))

# iterate over the length of x array to access the marks and calculate the standard deviation 
for k in range(len(x)):   
   st =st + ( (((int(x[k][1]))) -ave)) **2
std=sqrt( st/ len(x) )
print("The std deviation is:","{0:.2f}".format(std))



# search for the student with marks less than one standard deviation below the mean and that student will have to see a student adviser

rate= ave- std
for p in range(len(x)):
   if (int(x[p][1]))< rate:
      print("List of students who need to see an advisor:","\n",(x[p][0]),sep="")
   if (int(x[p][1])) > rate:
      pass
# close the file after processing the data in it
f.close()
