def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    numbers = [4, 2, 9, 1, 5, 6]
    target = 5

    print("Линейный поиск:", linear_search(numbers, target))

    sorted_numbers = sorted(numbers)
    print("Отсортированный массив:", sorted_numbers)
    print("Бинарный поиск:", binary_search(sorted_numbers, target))
