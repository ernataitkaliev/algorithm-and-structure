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


# Task 1 - Implement a Stack: push, pop, peek, isEmpty, size (тест на 10 элементах)
s = Stack()
for i in range(1, 11):
    s.push(i * 10)

print("Stack:", s.items)
print("Size =", s.size())
print("Peek =", s.peek())
print("Pop =", s.pop())
print("Pop =", s.pop())
print("Size after 2 pops =", s.size())
print("Is empty =", s.is_empty())
