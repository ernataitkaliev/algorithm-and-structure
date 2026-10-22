# Variant 2 - Task 2. Linked Lists - Find the Middle Node
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
