#Check palindrome number
N = int(input("Enter any Number: "))
N1 = N
rev = 0
while N > 0:
    rem = N % 10
    rev = rev*10 + rem
    N = N//10
print("Reverse Number: ", rev)
if rev == N1:
    print("Palindrome number")
else:
    print("Not Palindrome number")