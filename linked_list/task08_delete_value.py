# Task 8. Delete by Value
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

    def delete_value(self, value):
        if self.head is None:
            print("Element not found")
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        cur = self.head
        while cur.next:
            if cur.next.data == value:
                cur.next = cur.next.next
                return
            cur = cur.next
        print("Element not found")


lst = LinkedList()
for v in [10, 20, 30, 40]:
    lst.insert_at_end(v)
lst.delete_value(30)
lst.print_list()
lst.delete_value(99)
