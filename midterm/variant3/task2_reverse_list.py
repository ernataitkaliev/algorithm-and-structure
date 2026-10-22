# Variant 3 - Task 2. Linked Lists - Reverse a Singly Linked List
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
