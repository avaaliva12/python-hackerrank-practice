n = int(input("Enter Size of Tuple: "))
lst =[]
for i in range(n):
    val = int(input("Enter value: "))
    lst.append(val)

t = tuple(lst)
e = int(input("Enter an element of find its index: "))
for i in range(len(t)):
    if t[i] == e:
        print(i)
