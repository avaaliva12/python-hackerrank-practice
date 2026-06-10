n = int(input("Enter number of key-value pairs: "))
d = {}

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

print("Dictionary:", d)
#accessing keys
for key in d:
    print(key)

#accessing values
for value in d.values():
    print(value)

#accessing both key and values
for key in d:
    print(f"{key} = {d[key]}")

for key, value in d.items():
    print(key, ":", value)