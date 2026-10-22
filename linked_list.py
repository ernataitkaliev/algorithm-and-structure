# 1
# def second_largest(arr):
#     largest = None                    
#     second = None                     
#     for x in arr:
#         if largest is None or x > largest:      
#             second = largest                
#             largest = x
#         elif x != largest and (second is None or x > second):  
#             second = x                          
#     return second                               

# 2
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def build_list(values):
#     head = None
#     tail = None
#     for v in values:
#         new = Node(v)
#         if head is None:
#             head = new
#         else:
#             tail.next = new
#         tail = new
#     return head

# def list_to_text(head):
#     text = ""
#     cur = head
#     while cur:
#         text += str(cur.data) + " -> "
#         cur = cur.next
#     return text + "NULL"

# def remove_duplicates(head):
#     cur = head
#     while cur:
#         runner = cur
#         while runner.next:
#             if runner.next.data == cur.data:
#                 runner.next = runner.next.next
#             else:
#                 runner = runner.next
#         cur = cur.next
#     return head

# head = build_list([4, 2, 4, 7, 2, 9])
# print("Before:", list_to_text(head))
# head = remove_duplicates(head)
# print("After: ", list_to_text(head))

# 3
# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, value):
#         self.items.append(value)

#     def pop(self):
#         if self.is_empty():
#             return None
#         return self.items.pop()

#     def is_empty(self):
#         return len(self.items) == 0

# def is_balanced(text):
#     st = Stack()
#     pairs = {")": "(", "]": "[", "}": "{"}
#     for ch in text:
#         if ch in "([{":
#             st.push(ch)
#         elif ch in ")]}":
#             if st.is_empty() or st.pop() != pairs[ch]:
#                 return False
#     return st.is_empty()

# for expr in ("{[()]}", "{[(])}", "((", "())"):
#     print('"' + expr + '" ->', is_balanced(expr))

# 4
# class Queue:
#     def __init__(self):
#         self.items = []

#     def enqueue(self, value):
#         self.items.append(value)

#     def dequeue(self):
#         if self.is_empty():
#             return None
#         return self.items.pop(0)

#     def is_empty(self):
#         return len(self.items) == 0

# def generate_binary(n):
#     result = []
#     q = Queue()
#     q.enqueue("1")
#     for _ in range(n):
#         current = q.dequeue()
#         result.append(current)
#         q.enqueue(current + "0")
#         q.enqueue(current + "1")
#     return result

# print("N = 5 ->", ", ".join(generate_binary(5)))

# 5
# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# def bst_insert(root, key):
#     if root is None:
#         return TreeNode(key)
#     cur = root
#     while True:
#         if key < cur.value:
#             if cur.left is None:
#                 cur.left = TreeNode(key)
#                 break
#             cur = cur.left
#         else:
#             if cur.right is None:
#                 cur.right = TreeNode(key)
#                 break
#             cur = cur.right
#     return root

# def bst_search(root, key):
#     cur = root
#     while cur:
#         if key == cur.value:
#             return True
#         if key < cur.value:
#             cur = cur.left
#         else:
#             cur = cur.right
#     return False

# root = None
# for key in (50, 30, 70, 20, 40, 60, 80):
#     root = bst_insert(root, key)

# print("Search 40 ->", "Found" if bst_search(root, 40) else "Not found")
# print("Search 99 ->", "Found" if bst_search(root, 99) else "Not found")


# 6
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



