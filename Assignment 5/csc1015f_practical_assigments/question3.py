# program to simulate a vending machine

cost = eval(input("Enter the cost (in cents):\n"))
deposit = 0

while deposit < cost:
    dep = eval(input("Deposit a coin or note (in cents):\n"))
    deposit = deposit + dep

    if deposit >= cost:
        change = deposit - cost
        while change != 0:
            print("Your change is:")
            if change >= 500:
                print((change//500), "x R5")
                change = (change%500)
            if change >= 200:
                print((change//200), "x R2")
                change = (change%200)
            if change >= 100:
                print((change//100), "x R1")
                change = (change%100)
            if change >= 50:
                print((change//50), "x 50c")
                change = (change%50)
            if change >= 20:
                print((change//20), "x 20c")
                change = (change%20)
            if change >= 10:
                print((change//10), "x 10c")
                change = (change%10)
            if change >= 5:
                print((change//5), "x 5c")
                change = (change%5)
                
        else: 
            break
                
            
