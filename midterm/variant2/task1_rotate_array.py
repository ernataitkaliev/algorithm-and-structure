# Variant 2 - Task 1. Arrays - Rotate an Array
def reverse_part(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def rotate_right(arr, k):
    n = len(arr)
    if n == 0:
        return arr
    k = k % n
    reverse_part(arr, 0, n - 1)
    reverse_part(arr, 0, k - 1)
    reverse_part(arr, k, n - 1)
    return arr

print("k = 2 ->", rotate_right([1, 2, 3, 4, 5, 6], 2))
print("k = 8 ->", rotate_right([1, 2, 3, 4, 5, 6], 8))
