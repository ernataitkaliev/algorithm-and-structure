n = 6
mas = [1, 2, 4, 5, 6, 9]
target = 5

low = 0
high = n - 1
result = -1

while low <= high:
    mid = (low + high) // 2
    if mas[mid] == target:
        result = mid
        break
    elif mas[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

print(result)
