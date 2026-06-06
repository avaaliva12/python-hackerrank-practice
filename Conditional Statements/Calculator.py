#Menu-driven calculator
print("--------WELCOME--------")
n1 = int(input("Enter number: "))
n2 = int(input("Enter number: "))

print("1. Add 2. Subtract 3. Multiply 4. Division")
i = int(input("Enter your Choice: "))
if i == 1:
    print(n1+n2)
elif i == 2:
    print(n1-n2)
elif i == 3:
    print(n1*n2)
elif i == 4:
    print(n1/n2)
else:
    print("Invalid Choice")