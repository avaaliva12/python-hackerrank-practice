#Sum of first N natural numbers
N = int(input("Enter Range: "))
sum =0
for i in range(1,N+1):
    sum += i
print("Sum: ", sum)