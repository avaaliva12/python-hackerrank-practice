#Factorial of a number
N = int(input("Enter Range: "))
fact = 1
if N == 0:
    print("Factorial: ", fact)
else:
    for i in range(1,N+1):
        fact = fact * i
    print("Factorial: ", fact)