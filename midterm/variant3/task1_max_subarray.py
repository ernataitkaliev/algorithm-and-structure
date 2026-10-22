# Variant 3 - Task 1. Arrays - Maximum Sum of a Subarray
def max_subarray(arr):
    best = current = arr[0]
    start = best_start = best_end = 0
    for i in range(1, len(arr)):
        if current < 0:
            current = arr[i]
            start = i
        else:
            current += arr[i]
        if current > best:
            best = current
            best_start = start
            best_end = i
    return best, arr[best_start:best_end + 1]

total, part = max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print("Max sum =", total, "subarray =", part)
print("All negative:", max_subarray([-5, -2, -8]))
