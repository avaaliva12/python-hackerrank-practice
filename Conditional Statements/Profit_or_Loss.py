#Find profit or loss
CP = float(input("Enter Cost Price: "))
SP = float(input("Enter Selling Price: "))
if CP < SP:
    Profit = SP - CP
    print("Profit is: ", Profit)
else: 
    Loss = CP - SP
    print("Loss is: ", Loss)
