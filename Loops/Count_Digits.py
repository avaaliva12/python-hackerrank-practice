#Count digits
N = int(input("Enter any Number: "))
c = 0
while N > 0:
    rem = N % 10
    c+=1
    N = N // 10
print("Count digits: ", c)