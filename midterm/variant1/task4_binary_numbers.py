# Variant 1 - Task 4. Queues - Generate Binary Numbers
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

def generate_binary(n):
    result = []
    q = Queue()
    q.enqueue("1")
    for _ in range(n):
        current = q.dequeue()
        result.append(current)
        q.enqueue(current + "0")
        q.enqueue(current + "1")
    return result

print("N = 5 ->", ", ".join(generate_binary(5)))
