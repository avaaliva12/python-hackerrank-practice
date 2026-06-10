n = int(input("Enter number of key-value pairs: "))
d = {}

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

key = input("Enter key to update: ")

if key in d:
    value = input("Enter new value: ")
    d[key] = value
    print("Updated Dictionary:", d)
else:
    print("Key not found")