n = int(input("Enter size of set: "))

s = set()

for i in range(n):
    val = int(input("Enter value: "))
    s.add(val)

print("Original Set:", s)

x = int(input("Enter element to remove: "))

if x in s:
    s.remove(x)
    print("Updated Set:", s)
else:
    print("Element not found")