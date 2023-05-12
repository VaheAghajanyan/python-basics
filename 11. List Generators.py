a = [1, 2, 3, 4, 5]

range = [num *3 for num in range (1, 6)]
print(range)

lessThanThree = [num for num in a if num < 3]
print(lessThanThree)

words = ["hello", "say", "goodbye", "guitar"]
filtered = [word for word in words if len(word) < 5]
print(filtered)