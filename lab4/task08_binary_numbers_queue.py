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


# Task 8 - Generate Binary Numbers Using a Queue
def generate_binary(n):
    result = []
    q = Queue()
    q.enqueue("1")
    for i in range(n):
        current = q.dequeue()
        result.append(current)
        q.enqueue(current + "0")
        q.enqueue(current + "1")
    return result


N = 5
for b in generate_binary(N):
    print(b)
