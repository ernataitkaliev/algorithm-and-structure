# Variant 1 - Task 5. Trees - Binary Search Tree Search
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
