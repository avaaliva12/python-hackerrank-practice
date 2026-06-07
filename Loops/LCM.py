#Find LCM
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

a, b = n1, n2

while b != 0:
    a, b = b, a % b

gcd = a
lcm = (n1 * n2) // gcd

print("LCM =", lcm)