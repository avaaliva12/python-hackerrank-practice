#method 1
t = tuple(map(int, input("Enter numbers separated by space: ").split()))
print("Tuple:", t)

#method 2
t = tuple(input("Enter words separated by space: ").split())
print("Tuple:", t)

#method 3
n = int(input("Enter number of elements: "))

lst = []
for i in range(n):
    x = int(input("Enter element: "))
    lst.append(x)

t = tuple(lst)
print("Tuple:", t)
