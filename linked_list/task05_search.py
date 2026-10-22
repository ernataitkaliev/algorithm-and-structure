# Task 5. Search for an Element
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

    def search(self, value):
        cur = self.head
        while cur:
            if cur.data == value:
                return True
            cur = cur.next
        return False


lst = LinkedList()
for v in [10, 25, 30, 45]:
    lst.insert_at_end(v)
print("Search 30 ->", "Found" if lst.search(30) else "Not Found")
print("Search 50 ->", "Found" if lst.search(50) else "Not Found")
