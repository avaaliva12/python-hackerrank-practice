#Find largest element.
l = []
n = int(input("Enter size of the List: "))
for i in range(n):
    val = int(input("Enter value: "))
    l.append(val)

largest = max(l)
print("List: ", l)
print("Largest: ", largest)