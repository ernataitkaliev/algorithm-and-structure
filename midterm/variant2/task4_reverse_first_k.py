# Variant 2 - Task 4. Queues - Reverse the First K Elements
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

def reverse_first_k(queue, k):
    st = Stack()
    for _ in range(k):
        st.push(queue.dequeue())
    while not st.is_empty():
        queue.enqueue(st.pop())
    for _ in range(queue.size() - k):
        queue.enqueue(queue.dequeue())
    return queue

for k in (3, 0, 5):
    q = Queue()
    for v in [1, 2, 3, 4, 5]:
        q.enqueue(v)
    reverse_first_k(q, k)
    print("K =", k, "->", q.items)
