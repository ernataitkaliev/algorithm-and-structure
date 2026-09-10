n = 6
mas = [4, 2, 9, 1, 5, 6]
target = 5

result = -1
for i in range(n):
    if mas[i] == target:
        result = i
        break

print(result)
