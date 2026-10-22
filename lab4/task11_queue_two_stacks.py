class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Task 11 - Implement a Queue Using Two Stacks
class QueueTwoStacks:
    def __init__(self):
        self.in_stack = Stack()    # сюда добавляем
        self.out_stack = Stack()   # отсюда достаём

    def enqueue(self, value):
        self.in_stack.push(value)

    def _move(self):
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())

    def dequeue(self):
        self._move()
        return self.out_stack.pop()

    def peek(self):
        self._move()
        return self.out_stack.peek()

    def is_empty(self):
        return self.in_stack.is_empty() and self.out_stack.is_empty()


q = QueueTwoStacks()
for v in [1, 2, 3]:
    q.enqueue(v)
print("Dequeue:", q.dequeue())     # 1
q.enqueue(4)
print("Peek:", q.peek())           # 2
print("Dequeue:", q.dequeue(), q.dequeue(), q.dequeue())   # 2 3 4
print("Is empty:", q.is_empty())

# Почему это FIFO: при переносе из in_stack в out_stack порядок переворачивается,
# и самый старый элемент оказывается сверху out_stack - он и выходит первым.
