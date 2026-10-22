# Task 9. Find the Maximum Element
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

    def find_max(self):
        cur = self.head
        biggest = cur.data
        while cur:
            if cur.data > biggest:
                biggest = cur.data
            cur = cur.next
        return biggest


lst = LinkedList()
for v in [15, 7, 32, 4, 18]:
    lst.insert_at_end(v)
print("Maximum =", lst.find_max())
