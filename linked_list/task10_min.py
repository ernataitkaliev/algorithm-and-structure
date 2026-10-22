# Task 10. Find the Minimum Element
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        new = Node(value)
        if self.head is None:
            self.head = new
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new

    def print_list(self):
        cur = self.head
        text = ""
        while cur:
            text += str(cur.data) + " -> "
            cur = cur.next
        print(text + "NULL")

    def find_min(self):
        cur = self.head
        smallest = cur.data
        while cur:
            if cur.data < smallest:
                smallest = cur.data
            cur = cur.next
        return smallest


lst = LinkedList()
for v in [25, 8, 17, 3, 42]:
    lst.insert_at_end(v)
print("Minimum =", lst.find_min())
