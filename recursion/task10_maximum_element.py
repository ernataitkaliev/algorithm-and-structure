# Task 10. Find the Maximum Element
def array_max(arr):
    if len(arr) == 1:
        return arr[0]
    m = array_max(arr[1:])
    if arr[0] > m:
        return arr[0]
    return m

print(array_max([4, 8, 2, 15, 7]))
