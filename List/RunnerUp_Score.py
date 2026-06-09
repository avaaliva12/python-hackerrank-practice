arr = [2, 3, 6, 6, 5]

first = second = float('-inf')

for i in arr:
    if i > first:
        second = first
        first = i
    elif first > i > second:
        second = i

print("Runner-up score:", second)