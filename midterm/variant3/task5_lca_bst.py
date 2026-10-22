# Variant 3 - Task 5. Trees - Lowest Common Ancestor in a BST
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
