# program to simulate a simple BBS (Bulletin Board System)

def main():  
    msg = "no message yet"
    while True:
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        c = input("Enter your selection:\n")

        if c.upper() == "E":
            msg = input("Enter the message:\n")
        elif c.upper() == "V":
            print("The message is: " + msg)
        elif c.upper() == "L":
            print("List of files: 42.txt, 1015.txt")
        elif c.upper() == "D":
            d = input("Enter the filename:\n")
            if d == "1015.txt":
                print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
            elif d == "42.txt":
                print("The meaning of life is blah blah blah ...")
            else:
                print("File not found")
        elif c.upper() == "X":
            print("Goodbye!")        
            break
        else:
            print("no message yet")
    else:
        main()

main()