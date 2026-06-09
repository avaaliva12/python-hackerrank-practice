nums = [1, 2, 3, 4, 5]

squares = [x*x for x in nums]

print(squares)

evens = [x for x in nums if x % 2 == 0]
#evens = [x % 2 == 0 for x in nums] # gives result in true false
print(evens)