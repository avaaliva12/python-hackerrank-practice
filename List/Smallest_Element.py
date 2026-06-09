l = []
n = int(input("Enter size of the List: "))
for i in range(n):
    val = int(input("Enter value: "))
    l.append(val)

smallest = min(l)
print("List: ", l)
print("Smallest: ", smallest)