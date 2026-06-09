l = []
n = int(input("Enter size of the List: "))
for i in range(n):
    val = int(input("Enter value: "))
    l.append(val)
sum = 0
for j in l:
    sum+=j

avg = sum/n
print("Average Of all Elements: ", avg)