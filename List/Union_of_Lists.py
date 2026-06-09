l1 = []
n = int(input("Enter size of the List1: "))
for i in range(n):
    val = int(input("Enter value: "))
    l1.append(val)
l2 = []
n = int(input("Enter size of the List2: "))
for i in range(n):
    val = int(input("Enter value: "))
    l2.append(val)
union = []

for i in l1 + l2:
    if i not in union:
        union.append(i)

print("Union of lists:", union)
