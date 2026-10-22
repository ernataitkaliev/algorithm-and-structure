# Task 19. N-Queens Problem
def is_safe(cols, row, col):
    for r in range(row):
        if cols[r] == col or abs(cols[r] - col) == row - r:
            return False
    return True

def queens(cols, row, n):
    if row == n:
        print(cols)
        return
    for col in range(n):
        if is_safe(cols, row, col):
            cols.append(col)
            queens(cols, row + 1, n)
            cols.pop()

queens([], 0, 4)
