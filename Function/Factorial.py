def factorials(n):
    fact = 1
    if n == 0:
        return fact
    else:
        for i in range(1,n+1):
            fact *= i
        return fact
    
fact = factorials(3)
print("Factorial of 3: ", fact)
fact = factorials(0)
print("Factorial of 0: ", fact)
fact = factorials(1)
print("Factorial of 1: ", fact)