# Task 2. Insert at the Beginning
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

    def insert_at_beginning(self, value):
        new = Node(value)
        new.next = self.head
        self.head = new


lst = LinkedList()
for v in [20, 30, 40]:
    lst.insert_at_end(v)
lst.insert_at_beginning(10)
lst.print_list()
