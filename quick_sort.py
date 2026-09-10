n = 6
mas = [4, 2, 9, 1, 5, 6]

stack = [(0, n - 1)]

while stack:
    low, high = stack.pop()
    if low < high:
        pivot = mas[high]
        i = low - 1
        for j in range(low, high):
            if mas[j] <= pivot:
                i += 1
                mas[i], mas[j] = mas[j], mas[i]
        mas[i + 1], mas[high] = mas[high], mas[i + 1]
        p = i + 1
        stack.append((low, p - 1))
        stack.append((p + 1, high))

print(mas)
