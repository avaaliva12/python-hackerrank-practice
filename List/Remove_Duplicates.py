l = []
n = int(input("Enter size of the List: "))
for i in range(n):
    val = int(input("Enter value: "))
    l.append(val)

l1 = []
for i in l:
    if i not in l1:
        l1.append(i)

print("After removing duplicate elements: ", l1)