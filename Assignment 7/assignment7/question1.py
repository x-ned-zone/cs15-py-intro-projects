# Python program where the user can enter a list of strings followed by the sentinel "DONE" and the list of strings is then printed out right-aligned with the longest string.

# promp the user for an input of strings 
string=input("Enter strings (end with DONE):\n")
count=0
# create an empty list/array for storage of the strings
List_str=[]
# loop over the input of stirngs until user terminate by DONE
while string!='DONE':
    # store the strings on the list/array
    List_str.append(string)
    if count<len(string):
        count=len(string)
    string=input()

print()
print("Right-aligned list:")
# iterate over the list to format the strings right-aligned with the longest strings
for i in List_str:
    print(("{0:>"+str(count)+"}").format(i))
