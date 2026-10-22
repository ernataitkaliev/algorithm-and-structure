# Variant 3 - Task 6. Trees - Count Leaf Nodes
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
