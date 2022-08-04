# Program to count the number of votes for each political party in an election

print("Independent Electoral Commission")
print("--------------------------------")
# get names and split into words 

name=input("Enter the names of parties (terminated by DONE):\n")

ls_names=[]
# storage for counters
c_votes = {}

while name!="DONE":
    ls_names.append(name)
    name=input()


print() 
print("Vote counts:") 
# iterate over every item in the array/list to count the number of its occurrences
for name_i in ls_names:
    if name_i in c_votes:
        c_votes[name_i] += 1 
    else: 
    	c_votes[name_i] = 1 
# now print the count of occurrences with the votes left aligned and format the party names in afield wit width=10
for name_k in sorted(c_votes.keys()): 
    print (("{0:<10}").format(name_k),'-', c_votes[name_k]) 


