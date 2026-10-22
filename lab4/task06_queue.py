class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Task 6 - Implement a Queue: enqueue, dequeue, front, isEmpty, size (FIFO)
q = Queue()
for v in [1, 2, 3, 4, 5]:
    q.enqueue(v)

print("Queue:", q.items)
print("Front =", q.front())
print("Size =", q.size())

print("Dequeue order (FIFO):", end=" ")
while not q.is_empty():
    print(q.dequeue(), end=" ")
print()
print("Is empty =", q.is_empty())
