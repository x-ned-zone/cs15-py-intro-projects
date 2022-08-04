# Python program with a recursive function to calculate whether or not a string is a palindrome (reads the same if reversed). 

# prompt the user for an input 
string=input("Enter a string:\n")
# define the functin of a palindrome 
def Palindrome(string): 
    # b is the lenghth of the string to be compare to c later
    b=len(string) 
    # initialise c to zero 
    c=0 
    # iterate over the string in its lenghth
    for i in range(b):
        # compare each character on the string from the right of the string with the other character from the end of the string 
        if string[i]==string[-(i+1)]: 
            # if the characters are equal....increment c by one
            c=c+1 
    # if all the characters from either side in the string are equal while iteration occurs then it means that c will reach the lenghth of the string....ie..c=b...then from there the string is a palindrome.
    if c==b: 
        print("Palindrome!")
     #else b and c are not equal meaning that some characters or all the characters in the string are equal from either side...then thats not a palindrome
    else: 
        print("Not a palindrome!") 
# i'm calling the function with the input from the user to run the program recursively
Palindrome(string) 

    