# Task 15. Sort a Linked List
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

    def sort(self):
        swapped = True
        while swapped:
            swapped = False
            cur = self.head
            while cur and cur.next:
                if cur.data > cur.next.data:
                    cur.data, cur.next.data = cur.next.data, cur.data
                    swapped = True
                cur = cur.next


lst = LinkedList()
for v in [40, 10, 30, 20, 50]:
    lst.insert_at_end(v)
lst.sort()
lst.print_list()
