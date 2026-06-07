#Check prime number.
N = int(input("Enter any Number: "))
d = 0
for i in range(1, N+1):
    if N % i == 0:
        d += 1

if d == 2:
    print("Prime Number")
else:
    print("Not Prime Number")