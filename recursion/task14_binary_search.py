# Task 14. Recursive Binary Search
def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    return binary_search(arr, target, left, mid - 1)

arr = [2, 4, 7, 10, 15, 21]
print(binary_search(arr, 15, 0, len(arr) - 1))
