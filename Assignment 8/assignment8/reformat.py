# Python program to reformat a text file so that all lines are at most a given length
# Masixole Ntshinga
# 30 April 2012

name = []

filename= input("Enter the input filename:\n")
create=input("Enter the output filename:\n")
width= eval(input("Enter the line width:\n"))
# open the file with data
file = open (filename, "r")
test = file.read ()

file.close ()

texts = test.split("\n\n")# split for the space

for test in texts:
    name.append(test.replace("\n"," "))# new line

f= open(create,"w")
for sent in name:# iterate ,create new sentence
    wordz=sent.split(' ')
    line=''
    
    for i in wordz:
        if len(line+i) <= width:
            line= line+i+" "
        else:
            print(line,file=f)
            line =i+' '
    print(line,file=f)
    print(file=f)
f.close()

   
   