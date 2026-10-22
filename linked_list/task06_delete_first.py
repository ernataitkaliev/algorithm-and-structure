# Task 6. Delete the First Node
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

    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next


lst = LinkedList()
for v in [10, 20, 30, 40]:
    lst.insert_at_end(v)
lst.delete_first()
lst.print_list()
empty = LinkedList()
empty.delete_first()
