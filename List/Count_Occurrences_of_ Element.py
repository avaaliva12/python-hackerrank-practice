l = []
n = int(input("Enter size of the List: "))
for i in range(n):
    val = int(input("Enter value: "))
    l.append(val)

element = int(input("Enter element to count: "))

count = 0

for num in l:
    if num == element:
        count += 1
 
print(f"{element} occure {count} times in list")

"""
numbers = [10, 20, 30, 20, 40, 20]

element = int(input("Enter element to count: "))

count = numbers.count(element)

print(f"{element} occurs {count} times")
"""