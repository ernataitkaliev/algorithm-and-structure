# Task 15. Tower of Hanoi
def hanoi(n, a, c, b):
    if n == 0:
        return
    hanoi(n - 1, a, b, c)
    print("Move disk", n, "from", a, "to", c)
    hanoi(n - 1, b, c, a)

hanoi(3, "A", "C", "B")
