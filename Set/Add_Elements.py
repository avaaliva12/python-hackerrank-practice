n = int(input("Enter size: "))

s = set()

for i in range(n):
    val = int(input("Enter value: "))
    s.add(val)
print("Set =", s)
e = int(input("Enter an element to be added:"))
s.add(e)
print("Set =", s)