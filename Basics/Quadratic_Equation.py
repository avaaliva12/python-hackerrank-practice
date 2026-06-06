#Find the roots of a quadratic equation
import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = b**2 - 4*a*c

if d > 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print("Root 1 =", r1)
    print("Root 2 =", r2)

elif d == 0:
    r = -b / (2*a)
    print("Both roots are equal =", r)

else:
    real = -b / (2*a)
    imag = math.sqrt(-d) / (2*a)
    print("Root 1 =", real, "+", imag, "i")
    print("Root 2 =", real, "-", imag, "i")