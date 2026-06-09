l = []
n = int(input("Enter size of the List: "))
for i in range(n):
    val = int(input("Enter value: "))
    l.append(val)
l2 = []
for i in range (len(l)-1,-1,-1):
    l2.append(l[i])

print("Reverse List: ", l2)