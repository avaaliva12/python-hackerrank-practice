s = input("Enter a string: ")
rev = ""
original = s

for i in range(len(s) - 1, -1, -1):
    rev += s[i]

print("Reversed string:", rev)

if original == rev:
    print("Palindrome")
else:
    print("Not Palindrome")