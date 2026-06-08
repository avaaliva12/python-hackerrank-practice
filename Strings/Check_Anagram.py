"""
Two strings are anagrams if they contain the same 
characters with the same frequency, regardless of order.
"""
s1 = input("Enter any String 1: ")
s2 = input("Enter any String 2: ")

if len(s1) != len(s2):
    print("Not Anagram")
else:
    s1 = sorted(s1)
    s2 = sorted(s2)

    if s1 == s2:
        print("Anagram")
    else:
        print("Not Anagram")

"""
s1 = input("Enter any String 1: ").lower()
s2 = input("Enter any String 2: ").lower()

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")
"""