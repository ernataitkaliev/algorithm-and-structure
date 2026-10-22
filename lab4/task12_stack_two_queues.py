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


# Task 12 - Implement a Stack Using Two Queues
class StackTwoQueues:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, value):
        self.q2.enqueue(value)                 # новый элемент в пустую очередь
        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.dequeue()) # затем все старые за ним
        self.q1, self.q2 = self.q2, self.q1    # меняем очереди местами

    def pop(self):
        return self.q1.dequeue()

    def peek(self):
        return self.q1.front()

    def is_empty(self):
        return self.q1.is_empty()


s = StackTwoQueues()
for v in [1, 2, 3]:
    s.push(v)
print("Peek:", s.peek())                       # 3
print("Pop:", s.pop(), s.pop(), s.pop())       # 3 2 1 (LIFO)
print("Is empty:", s.is_empty())
