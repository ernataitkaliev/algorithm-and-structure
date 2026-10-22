#1
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


#2
def sum_to(n):
    if n == 0:
        return 0
    return n + sum_to(n - 1)

print(sum_to(5))


#3
def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)

print(power(2, 5))


#4
def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

print(count_digits(58321))


#5
def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

print(sum_digits(58321))


#6
def reverse_num(n, result=0):
    if n == 0:
        return result
    return reverse_num(n // 10, result * 10 + n % 10)

print(reverse_num(12345))


#7
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(7))


#8
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))


#9
def array_sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + array_sum(arr[1:])

print(array_sum([2, 4, 6, 8]))


#10
def array_max(arr):
    if len(arr) == 1:
        return arr[0]
    m = array_max(arr[1:])
    if arr[0] > m:
        return arr[0]
    return m

print(array_max([4, 8, 2, 15, 7]))


#11
def count_x(arr, x):
    if len(arr) == 0:
        return 0
    if arr[0] == x:
        return 1 + count_x(arr[1:], x)
    return count_x(arr[1:], x)

print(count_x([2, 5, 2, 8, 2, 9], 2))


#12
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("level"))
print(is_palindrome("hello"))


#13
def reverse_str(s):
    if len(s) == 0:
        return ""
    return reverse_str(s[1:]) + s[0]

print(reverse_str("algorithm"))


#14
def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    return binary_search(arr, target, left, mid - 1)

arr = [2, 4, 7, 10, 15, 21]
print(binary_search(arr, 15, 0, len(arr) - 1))


#15
def hanoi(n, a, c, b):
    if n == 0:
        return
    hanoi(n - 1, a, b, c)
    print("Move disk", n, "from", a, "to", c)
    hanoi(n - 1, b, c, a)

hanoi(3, "A", "C", "B")


#16
def subsets(arr, i, cur):
    if i == len(arr):
        print(cur)
        return
    subsets(arr, i + 1, cur)
    subsets(arr, i + 1, cur + [arr[i]])

subsets([1, 2, 3], 0, [])


#17
def permute(prefix, rest):
    if rest == "":
        print(prefix)
        return
    for i in range(len(rest)):
        permute(prefix + rest[i], rest[:i] + rest[i+1:])

permute("", "ABC")


#18
def solve(maze, r, c, path):
    if r < 0 or c < 0 or r >= len(maze) or c >= len(maze[0]):
        return False
    if maze[r][c] != 0:
        return False
    maze[r][c] = 2
    path.append((r, c))
    if r == len(maze) - 1 and c == len(maze[0]) - 1:
        return True
    if (solve(maze, r, c + 1, path) or solve(maze, r + 1, c, path) or
            solve(maze, r, c - 1, path) or solve(maze, r - 1, c, path)):
        return True
    path.pop()
    return False

maze = [[0, 1, 0, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0],
        [0, 0, 0, 0]]
path = []
if solve(maze, 0, 0, path):
    print(path)


#19
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


#20
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(node):
    if node is None:
        return
    print(node.value, end=" ")
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.value, end=" ")
    inorder(node.right)

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value, end=" ")

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.right = Node(20)

preorder(root)
print()
inorder(root)
print()
postorder(root)
