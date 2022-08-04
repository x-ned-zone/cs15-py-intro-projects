# biology.py
def animal():
    print("Welcome to the Biology Expert")
    print("-----------------------------")
    print("Answer the following questions by selecting from among the options.")
    A=input("The skeleton is (internal/external)?\n")
    if A=="internal":
        B=input("The fertilisation of eggs occurs (within the body/outside the body)?\n")
        if B=="within the body":
            C=input("Young are produced by (waterproof eggs/live birth)?\n")
            if C=="waterproof eggs":
                D=input("The skin is covered by (scales/feathers)?\n")
                if D=="scales":
                    print("Type of animal: Reptile")
                if D=="feathers":
                    print("Type of animal: Bird")
            if C=="live birth":
                print("Type of animal: Mammal")
        if B=="outside the body":
            E=input("It lives (in water/near water)?\n")
            if E=="in water":
                print("Type of animal: Fish")
            if E=="near water":
                print("Type of animal: Amphibian")
    if A=="external":
        print("Type of animal: Arthropod")
animal()
