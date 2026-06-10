n = int(input("Enter number of key-value pairs: "))
d = {}

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

print("Dictionary:", d)

k = input("Enter the key to be deleted: ")

if k in d:
    del d[k]
    print("Updated Dictionary:", d)
else:
    print(f"{k} Key not found")