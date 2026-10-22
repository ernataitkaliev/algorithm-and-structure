# Variant 1 - Task 2. Linked Lists - Remove Duplicates
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
