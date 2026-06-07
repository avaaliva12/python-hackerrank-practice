#Sum of digits
N = int(input("Enter any Number: "))
s = 0
while N > 0:
    rem = N % 10
    s+=rem
    N = N // 10
print("Count digits: ", s)