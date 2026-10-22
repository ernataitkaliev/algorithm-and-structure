# Task 6. Reverse a Number
def reverse_num(n, result=0):
    if n == 0:
        return result
    return reverse_num(n // 10, result * 10 + n % 10)

print(reverse_num(12345))
