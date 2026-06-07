#Find frequency of a character
s = input("Enter a string: ")
s = s.lower()
c = input("Enter a character: ")
d = 0
for i in s:
    if i == c:
        d +=1
print("frequency of a character: ", d)
