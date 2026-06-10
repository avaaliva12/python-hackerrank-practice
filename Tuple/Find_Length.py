n = int(input("Enter number of elements: "))

lst = []
for i in range(n):
    x = int(input("Enter element: "))
    lst.append(x)

t = tuple(lst)

print("Length of Tuple: ", len(t))
