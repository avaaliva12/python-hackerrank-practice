def reverse(str):
    l = len(str)
    rev = ""
    for i in range(l-1,-1,-1):
        rev = rev + str[i]
    
    return rev

rev = reverse("Aliva")
print("Reversed String: ", rev)