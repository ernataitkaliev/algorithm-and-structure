# ==============================================================
# MIDTERM - Algorithms and Data Structures
# Variant 1, Variant 2, Variant 3 (6 tasks in each).
# Every task is self-contained: it has its own classes and functions.
# ==============================================================


# ##############################################################
# #                        VARIANT 1                           #
# ##############################################################

# --------------------------------------------------------------
# V1 Task 1. Arrays - Find the Second Largest Element
# One pass, no sorting. Time: O(n), extra memory: O(1).
# --------------------------------------------------------------
print("\n===== VARIANT 1, Task 1: Second Largest Element =====")

def second_largest(arr):
    largest = None
    second = None
    for x in arr:
        if largest is None or x > largest:
            second = largest
            largest = x
        elif x != largest and (second is None or x > second):
            second = x
    return second

for data in ([12, 5, 8, 12, 9, 7], [5, 5, 5], [7]):
    result = second_largest(data)
    if result is None:
        print(data, "-> no second largest distinct element")
    else:
        print(data, "->", result)


# --------------------------------------------------------------
# V1 Task 2. Linked Lists - Remove Duplicates
# Keeps the first occurrence of each value. Time: O(n^2), memory: O(1).
# --------------------------------------------------------------
print("\n===== VARIANT 1, Task 2: Remove Duplicates =====")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def build_list(values):
    head = None
    tail = None
    for v in values:
        new = Node(v)
        if head is None:
            head = new
        else:
            tail.next = new
        tail = new
    return head

def list_to_text(head):
    text = ""
    cur = head
    while cur:
        text += str(cur.data) + " -> "
        cur = cur.next
    return text + "NULL"

def remove_duplicates(head):
    cur = head
    while cur:
        runner = cur
        while runner.next:
            if runner.next.data == cur.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        cur = cur.next
    return head

head = build_list([4, 2, 4, 7, 2, 9])
print("Before:", list_to_text(head))
head = remove_duplicates(head)
print("After: ", list_to_text(head))


# --------------------------------------------------------------
# V1 Task 3. Stacks - Balanced Brackets
# Opening bracket -> push, closing bracket -> pop and compare the type.
# --------------------------------------------------------------
print("\n===== VARIANT 1, Task 3: Balanced Brackets =====")

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def is_balanced(text):
    st = Stack()
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in text:
        if ch in "([{":
            st.push(ch)
        elif ch in ")]}":
            if st.is_empty() or st.pop() != pairs[ch]:
                return False
    return st.is_empty()

for expr in ("{[()]}", "{[(])}", "((", "())"):
    print('"' + expr + '" ->', is_balanced(expr))


# --------------------------------------------------------------
# V1 Task 4. Queues - Generate Binary Numbers
# Why a queue: numbers must come out in ascending order (FIFO).
# Each number x produces x+"0" and x+"1", which are the next ones in order.
# --------------------------------------------------------------
print("\n===== VARIANT 1, Task 4: Generate Binary Numbers =====")

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

def generate_binary(n):
    result = []
    q = Queue()
    q.enqueue("1")
    for _ in range(n):
        current = q.dequeue()
        result.append(current)
        q.enqueue(current + "0")
        q.enqueue(current + "1")
    return result

print("N = 5 ->", ", ".join(generate_binary(5)))


# --------------------------------------------------------------
# V1 Task 5. Trees - Binary Search Tree Search
# Search is iterative.
# Average time: O(log n). Worst case: O(n) (tree degenerates into a list).
# --------------------------------------------------------------
print("\n===== VARIANT 1, Task 5: BST Search =====")

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bst_insert(root, key):
    if root is None:
        return TreeNode(key)
    cur = root
    while True:
        if key < cur.value:
            if cur.left is None:
                cur.left = TreeNode(key)
                break
            cur = cur.left
        else:
            if cur.right is None:
                cur.right = TreeNode(key)
                break
            cur = cur.right
    return root

def bst_search(root, key):
    cur = root
    while cur:
        if key == cur.value:
            return True
        if key < cur.value:
            cur = cur.left
        else:
            cur = cur.right
    return False

root = None
for key in (50, 30, 70, 20, 40, 60, 80):
    root = bst_insert(root, key)

print("Search 40 ->", "Found" if bst_search(root, 40) else "Not found")
print("Search 99 ->", "Found" if bst_search(root, 99) else "Not found")


# --------------------------------------------------------------
# V1 Task 6. Trees - Tree Height
# Height = number of nodes on the longest root-to-leaf path, empty tree = 0.
# --------------------------------------------------------------
print("\n===== VARIANT 1, Task 6: Tree Height =====")

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
print("Height =", height(root))
print("Height of empty tree =", height(None))


# ##############################################################
# #                        VARIANT 2                           #
# ##############################################################

# --------------------------------------------------------------
# V2 Task 1. Arrays - Rotate an Array
# In place, three reversals. k % n handles k > n.
# Time: O(n), extra memory: O(1).
# --------------------------------------------------------------
print("\n===== VARIANT 2, Task 1: Rotate an Array =====")

def reverse_part(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def rotate_right(arr, k):
    n = len(arr)
    if n == 0:
        return arr
    k = k % n
    reverse_part(arr, 0, n - 1)
    reverse_part(arr, 0, k - 1)
    reverse_part(arr, k, n - 1)
    return arr

print("k = 2 ->", rotate_right([1, 2, 3, 4, 5, 6], 2))
print("k = 8 ->", rotate_right([1, 2, 3, 4, 5, 6], 8))


# --------------------------------------------------------------
# V2 Task 2. Linked Lists - Find the Middle Node
# slow moves 1 step, fast moves 2 steps, one pass.
# For an even number of nodes this returns the second middle node.
# --------------------------------------------------------------
print("\n===== VARIANT 2, Task 2: Middle Node =====")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def build_list(values):
    head = None
    tail = None
    for v in values:
        new = Node(v)
        if head is None:
            head = new
        else:
            tail.next = new
        tail = new
    return head

def find_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

print("10 -> 20 -> 30 -> 40 -> 50 :", find_middle(build_list([10, 20, 30, 40, 50])).data)
print("10 -> 20 -> 30 -> 40       :", find_middle(build_list([10, 20, 30, 40])).data)


# --------------------------------------------------------------
# V2 Task 3. Stacks - Evaluate a Postfix Expression
# Numbers go to the stack, an operator takes two numbers from it.
# Division is truncated toward zero.
# --------------------------------------------------------------
print("\n===== VARIANT 2, Task 3: Postfix Expression =====")

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

def divide_truncate(a, b):
    q = abs(a) // abs(b)
    if (a < 0) != (b < 0):
        q = -q
    return q

def evaluate_postfix(expr):
    st = Stack()
    for token in expr.split():
        if token in ("+", "-", "*", "/"):
            b = st.pop()
            a = st.pop()
            if token == "+":
                st.push(a + b)
            elif token == "-":
                st.push(a - b)
            elif token == "*":
                st.push(a * b)
            else:
                st.push(divide_truncate(a, b))
        else:
            st.push(int(token))
    return st.pop()

print('"12 3 4 * +" ->', evaluate_postfix("12 3 4 * +"))
print('"7 2 /"      ->', evaluate_postfix("7 2 /"))
print('"2 7 - 3 /"  ->', evaluate_postfix("2 7 - 3 /"))


# --------------------------------------------------------------
# V2 Task 4. Queues - Reverse the First K Elements
# 1) first K elements: queue -> stack (order flips)
# 2) stack -> back to the queue (they are now reversed)
# 3) the remaining N-K elements are moved from the front to the back
# --------------------------------------------------------------
print("\n===== VARIANT 2, Task 4: Reverse First K Elements =====")

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

def reverse_first_k(queue, k):
    st = Stack()
    for _ in range(k):
        st.push(queue.dequeue())
    while not st.is_empty():
        queue.enqueue(st.pop())
    for _ in range(queue.size() - k):
        queue.enqueue(queue.dequeue())
    return queue

for k in (3, 0, 5):
    q = Queue()
    for v in [1, 2, 3, 4, 5]:
        q.enqueue(v)
    reverse_first_k(q, k)
    print("K =", k, "->", q.items)


# --------------------------------------------------------------
# V2 Task 5. Trees - Validate a Binary Search Tree
# Every node must fit the range (low, high) inherited from ALL ancestors,
# not only from its direct parent.
# --------------------------------------------------------------
print("\n===== VARIANT 2, Task 5: Validate BST =====")

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_bst(node, low=None, high=None):
    if node is None:
        return True
    if low is not None and node.value <= low:
        return False
    if high is not None and node.value >= high:
        return False
    return is_bst(node.left, low, node.value) and is_bst(node.right, node.value, high)

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(12)
print("Root 10, 5, 15, 12 (left of 15) ->", is_bst(root))

wrong = TreeNode(10)
wrong.left = TreeNode(5)
wrong.right = TreeNode(15)
wrong.left.right = TreeNode(12)      # 12 > 10, but sits in the left subtree
print("12 as right child of 5          ->", is_bst(wrong))


# --------------------------------------------------------------
# V2 Task 6. Trees - Level-Order Traversal
# Queue: take a node, print it, add its children to the back.
# --------------------------------------------------------------
print("\n===== VARIANT 2, Task 6: Level-Order Traversal =====")

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

def level_order(root):
    result = []
    if root is None:
        return result
    q = Queue()
    q.enqueue(root)
    while not q.is_empty():
        node = q.dequeue()
        result.append(node.value)
        if node.left:
            q.enqueue(node.left)
        if node.right:
            q.enqueue(node.right)
    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(", ".join(str(v) for v in level_order(root)))


# ##############################################################
# #                        VARIANT 3                           #
# ##############################################################

# --------------------------------------------------------------
# V3 Task 1. Arrays - Maximum Sum of a Subarray (Kadane's algorithm)
# If the running sum is negative, it only hurts - start again from the current element.
# Time: O(n), memory: O(1).
# --------------------------------------------------------------
print("\n===== VARIANT 3, Task 1: Maximum Subarray Sum =====")

def max_subarray(arr):
    best = current = arr[0]
    start = best_start = best_end = 0
    for i in range(1, len(arr)):
        if current < 0:
            current = arr[i]
            start = i
        else:
            current += arr[i]
        if current > best:
            best = current
            best_start = start
            best_end = i
    return best, arr[best_start:best_end + 1]

total, part = max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print("Max sum =", total, "subarray =", part)
print("All negative:", max_subarray([-5, -2, -8]))


# --------------------------------------------------------------
# V3 Task 2. Linked Lists - Reverse a Singly Linked List
# Iterative, three pointers prev / cur / nxt, no new list.
# Time: O(n), extra memory: O(1).
# --------------------------------------------------------------
print("\n===== VARIANT 3, Task 2: Reverse a Linked List =====")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def build_list(values):
    head = None
    tail = None
    for v in values:
        new = Node(v)
        if head is None:
            head = new
        else:
            tail.next = new
        tail = new
    return head

def list_to_text(head):
    text = ""
    cur = head
    while cur:
        text += str(cur.data) + " -> "
        cur = cur.next
    return text + "NULL"

def reverse_list(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev

head = build_list([1, 2, 3, 4, 5])
print("Before:", list_to_text(head))
head = reverse_list(head)
print("After: ", list_to_text(head))


# --------------------------------------------------------------
# V3 Task 3. Stacks - Next Greater Element
# The stack keeps indexes of elements still waiting for a greater one.
# Each index is pushed and popped once, so time is O(n).
# --------------------------------------------------------------
print("\n===== VARIANT 3, Task 3: Next Greater Element =====")

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

def next_greater(arr):
    result = [-1] * len(arr)
    st = Stack()
    for i, x in enumerate(arr):
        while not st.is_empty() and arr[st.peek()] < x:
            result[st.pop()] = x
        st.push(i)
    return result

print([4, 5, 2, 10, 8], "->", next_greater([4, 5, 2, 10, 8]))


# --------------------------------------------------------------
# V3 Task 4. Queues - Implement a Queue Using Two Stacks
# enqueue -> push to in_stack. dequeue/peek -> if out_stack is empty,
# move everything from in_stack (order flips, the oldest element ends on top).
# Amortized time: every element is moved between stacks at most once,
# so n operations cost O(n) in total -> O(1) per operation.
# --------------------------------------------------------------
print("\n===== VARIANT 3, Task 4: Queue Using Two Stacks =====")

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

class QueueTwoStacks:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def is_empty(self):
        return self.in_stack.is_empty() and self.out_stack.is_empty()

    def enqueue(self, value):
        self.in_stack.push(value)

    def _move(self):
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, nothing to remove")
            return None
        self._move()
        return self.out_stack.pop()

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        self._move()
        return self.out_stack.peek()

q = QueueTwoStacks()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
first = q.dequeue()
second = q.peek()
print(first, "then", second)
q.dequeue()
q.dequeue()
q.dequeue()


# --------------------------------------------------------------
# V3 Task 5. Trees - Lowest Common Ancestor in a BST
# BST property: if both values are smaller than the node go left,
# if both are larger go right, otherwise the node is the LCA.
# Only one path is walked: O(h) time.
# --------------------------------------------------------------
print("\n===== VARIANT 3, Task 5: LCA in a BST =====")

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bst_insert(root, key):
    if root is None:
        return TreeNode(key)
    cur = root
    while True:
        if key < cur.value:
            if cur.left is None:
                cur.left = TreeNode(key)
                break
            cur = cur.left
        else:
            if cur.right is None:
                cur.right = TreeNode(key)
                break
            cur = cur.right
    return root

def lca(root, a, b):
    cur = root
    while cur:
        if a < cur.value and b < cur.value:
            cur = cur.left
        elif a > cur.value and b > cur.value:
            cur = cur.right
        else:
            return cur.value
    return None

root = None
for key in (20, 10, 30, 5, 15, 25, 35):
    root = bst_insert(root, key)

print("LCA(5, 15)  =", lca(root, 5, 15))
print("LCA(5, 35)  =", lca(root, 5, 35))
print("LCA(25, 35) =", lca(root, 25, 35))
print("LCA(10, 5)  =", lca(root, 10, 5))


# --------------------------------------------------------------
# V3 Task 6. Trees - Count Leaf Nodes
# Leaf = node without children. Empty tree gives 0.
# --------------------------------------------------------------
print("\n===== VARIANT 3, Task 6: Count Leaf Nodes =====")

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
print("Leaves =", count_leaves(root))
print("Leaves in empty tree =", count_leaves(None))
