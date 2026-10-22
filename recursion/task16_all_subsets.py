# Task 16. Generate All Subsets
def subsets(arr, i, cur):
    if i == len(arr):
        print(cur)
        return
    subsets(arr, i + 1, cur)
    subsets(arr, i + 1, cur + [arr[i]])

subsets([1, 2, 3], 0, [])
