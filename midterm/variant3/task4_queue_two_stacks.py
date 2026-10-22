# Variant 3 - Task 4. Queues - Implement a Queue Using Two Stacks
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

class QueueTwoStacks:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def is_empty(self):
        return self.in_stack.is_empty() and self.out_stack.is_empty()

    def enqueue(self, value):
        self.in_stack.push(value)

    def _move(self):
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, nothing to remove")
            return None
        self._move()
        return self.out_stack.pop()

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        self._move()
        return self.out_stack.peek()

q = QueueTwoStacks()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
first = q.dequeue()
second = q.peek()
print(first, "then", second)
q.dequeue()
q.dequeue()
q.dequeue()
