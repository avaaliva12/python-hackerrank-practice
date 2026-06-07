#Count vowels and consonants
str = input("Enter a word: ")
str = str.lower()
v = 0
c = 0
for i in str:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        v +=1
    else:
        c +=1

print("vowel: ", v)
print("consonent: ", c)