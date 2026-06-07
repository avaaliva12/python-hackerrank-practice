#Find GCD using loops
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

gcd = 1

for i in range(1, min(n1, n2) + 1):
    if n1 % i == 0 and n2 % i == 0:
        gcd = i

print("GCD =", gcd)

"""n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

a, b = n1, n2

while b != 0:
    a, b = b, a % b

gcd = a"""