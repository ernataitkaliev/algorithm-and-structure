# Task 11. Count Occurrences
def count_x(arr, x):
    if len(arr) == 0:
        return 0
    if arr[0] == x:
        return 1 + count_x(arr[1:], x)
    return count_x(arr[1:], x)

print(count_x([2, 5, 2, 8, 2, 9], 2))
