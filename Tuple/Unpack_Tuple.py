t = tuple(map(int, input("Enter 3 numbers: ").split()))
print(t)
a, b, c = t

print("a =", a)
print("b =", b)
print("c =", c)

t = (1, 2, 3, 4, 5)

a, *b = t

print(a)
print(b)