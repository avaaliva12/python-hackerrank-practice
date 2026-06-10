def findmax(l):
    largest = l[0]  # Assume first element is largest

    for i in l:
        if i > largest:
            largest = i

    return largest

lst = [10, 45, 23, 50, 4]
largest = findmax(lst)

print("Largest element:", largest)