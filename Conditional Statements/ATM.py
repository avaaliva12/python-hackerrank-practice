#ATM withdrawal simulation
Total_Amount = float(input("Enter Total balance: "))
PIN = int(input("Enter Pin Number: "))
if PIN == 1234:
    while 1:
        print("1. Check Balance 2. Deposite 3. Withdrawl 4. Exit")
        i = int(input("Enter your Choice: "))
        if i == 1:
            print("Balance = ", Total_Amount)
        elif i == 2:
            amount = float(input("Enter amount to deposite: "))
            Total_Amount += amount
        elif i ==3:
            wa = float(input("Enter amount to withdrawl: "))
            if Total_Amount < wa and Total_Amount == 0:
                print("amount can't be withdrawl")
            else:
                Total_Amount -= wa
        elif i == 4:
            print("Exiting....")
            break
else:
    print("Incorrect Password")
