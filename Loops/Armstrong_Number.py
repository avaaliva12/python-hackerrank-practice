#Check armstrong number
N = int(input("Enter any Number: "))
N1 = N
cub = 0
while N > 0:
    rem = N % 10
    cub = cub + rem**3
    N = N//10
print("Cube Number: ", cub)
if cub == N1:
    print("Armstrong number")
else:
    print("Not Armstrong number")