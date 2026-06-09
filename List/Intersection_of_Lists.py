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

l3 = []
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i] == l2[j]:
            l3.append(l1[i])

print("Intersection of Elements: ", l3)