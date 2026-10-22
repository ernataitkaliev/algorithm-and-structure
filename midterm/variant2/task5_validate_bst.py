# Variant 2 - Task 5. Trees - Validate a Binary Search Tree
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
wrong.left.right = TreeNode(12)
print("12 as right child of 5          ->", is_bst(wrong))
