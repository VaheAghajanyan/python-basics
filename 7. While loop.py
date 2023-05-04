total = 0
i1 = 0

while i1 < 5:
    total += i1
    i1 += 1

print(total)

myList = [0, 1, 2, 3, 4, 5, 6, 7]
total2 = 0
i2 = 0

while myList[i2] < 4:
    total2 += myList[i2]
    i2 += 1

print(total2)

i3 = 0

while i3 < 10:
    if i3 == 5:
        break
    print(i3)
    i3 += 1
