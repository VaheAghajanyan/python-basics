arr = [[1, 2 ,3],
       [4, 5, 6],
       [7, 8, 9]]

print(arr[1])

def print_matrix(arr):
    for array in arr:
        for j in array:
            print(j, end= ' ')
        print()

print_matrix(arr)