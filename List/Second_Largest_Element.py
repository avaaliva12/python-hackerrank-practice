l = []
n = int(input("Enter size of the List: "))
for i in range(n):
    val = int(input("Enter value: "))
    l.append(val)

l = sorted(l)
print("Second Largest Element: ", l[n-2])