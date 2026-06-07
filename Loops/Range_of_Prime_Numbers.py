N = int(input("Enter any Number: "))

for num in range(2, N + 1):
    d = 0

    for i in range(1, num + 1):
        if num % i == 0:
            d += 1

    if d == 2:
        print(num, end=" ")