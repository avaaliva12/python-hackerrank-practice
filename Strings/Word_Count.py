#Count words.
s = input("Enter any sentence: ")
s = s.strip()
#l = len(s)
c = 0
for i in s:
    if i == ' ':
        c +=1
w = c+1
print("No of Words in this sentence: ", w)
