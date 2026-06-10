n = int(input("Enter Size of Tuple: "))
lst =[]
for i in range(n):
    val = int(input("Enter value: "))
    lst.append(val)

t = tuple(lst)
print("Maximum value in Tuple: ", max(t))
print("Minimum value in Tuple: ", min(t))
