# Task 11. Count Even Numbers
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

    def count_even(self):
        count = 0
        cur = self.head
        while cur:
            if cur.data % 2 == 0:
                count += 1
            cur = cur.next
        return count


lst = LinkedList()
for v in [3, 8, 12, 7, 5, 20]:
    lst.insert_at_end(v)
print("Even numbers =", lst.count_even())
