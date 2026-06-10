n = int(input("Enter Size of Tuple: "))
lst =[]
for i in range(n):
    val = int(input("Enter value: "))
    lst.append(val)

t = tuple(lst)
print("Tuple: ", t)
s = int(input("Enter any element to find occurance: "))
count = 0
for i in t:
    if i == s:
        count += 1
    
if count > 0:
    print(f"{s} occured {count} time in tuple")
else:
    print(f"{s} is not available in this tuple")