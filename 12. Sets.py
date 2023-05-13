my_set = {1, 2, 3, 4, 5}
my_set.add(6)
my_set.remove(3)

if 4 in my_set:
    print("4 is in the set")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
union = set1.union(set2)

# Intersection
intersection = set1.intersection(set2)

# Difference
difference = set1.difference(set2)

# Symmetric difference
symmetric_difference = set1.symmetric_difference(set2)