for x in "banana":
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue

for x in range(2, 6):
  print(x)

for x in range(2, 30, 3):
  print(x)

my_list = ['apple', 'banana', 'cherry']

for i, item in enumerate(my_list):
    print(i, item)
