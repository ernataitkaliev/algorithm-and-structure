# Variant 2 - Task 6. Trees - Level-Order Traversal
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
