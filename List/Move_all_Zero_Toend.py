l = []
n = int(input("Enter size of the List: "))
for i in range(n):
    val = int(input("Enter value: "))
    l.append(val)
n = []
for i in l:
    if i != 0:
        n.append(i)

for i in l:
    if i == 0:
        n.append(i)

print("List After Shifting: ",n)