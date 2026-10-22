# Task 9. Recursive Array Sum
def array_sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + array_sum(arr[1:])

print(array_sum([2, 4, 6, 8]))
