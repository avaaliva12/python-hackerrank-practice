#Print even numbers up to N
N = int(input("Enter Range: "))
for i in range(1,N+1):
    if i % 2 == 0:
        print(i)