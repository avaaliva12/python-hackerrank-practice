#Replace a substring
s = input("Enter any String: ")
s1 = input("Enter any sub string from above string to be replaced: ")
s2 = input("Enter new sub string to be replaced with old one: ")
s = s.replace(s1, s2)
print(s)

"""
s = input("Enter a string: ")
old = input("Enter substring to replace: ")
new = input("Enter new substring: ")

index = s.find(old)

if index != -1:
    result = s[:index] + new + s[index + len(old):]
    print("Updated string:", result)
else:
    print("Substring not found")
"""