# program that uses a recursive function to count the number of pairs of consecutive characters in a string

lett=input("Enter a message:\n")

def letters(lett):
     if (len(lett))<2:
          return (0)
     elif lett[0]==lett[1]:
          return 1 + letters(lett[2:])
     
     else :
          return 0 + letters(lett[1:])
     
print("Number of pairs:",letters(lett))
    