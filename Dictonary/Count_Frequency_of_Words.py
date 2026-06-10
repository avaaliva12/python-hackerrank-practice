sentence = input("Enter a sentence: ")

words = sentence.split()
print(words)
d = {}

for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print("Frequency of words:")
for key, value in d.items():
    print(key, ":", value)