n = 6
mas = [4, 2, 9, 1, 5, 6]

for run in range(n - 1):
    for i in range(n - 1):
        if mas[i] > mas[i + 1]:
            mas[i], mas[i + 1] = mas[i + 1], mas[i]

print(mas)
