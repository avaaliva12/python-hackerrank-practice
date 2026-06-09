l1 = [1,2,3]
l2 = [4,5]

ml = l1+l2
print("Merged List using + operator:", ml)

l1.extend(l2)
print("Merged List using extend() operator:", l1)