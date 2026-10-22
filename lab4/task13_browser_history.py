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


# Task 13 - Browser History Simulation
class Browser:
    def __init__(self):
        self.back_stack = Stack()
        self.forward_stack = Stack()
        self.current = None

    def visit(self, page):
        if self.current is not None:
            self.back_stack.push(self.current)
        self.current = page
        self.forward_stack = Stack()    # после нового visit "вперёд" очищается
        print("Visit:", page)

    def back(self):
        if self.back_stack.is_empty():
            return self.current
        self.forward_stack.push(self.current)
        self.current = self.back_stack.pop()
        return self.current

    def forward(self):
        if self.forward_stack.is_empty():
            return self.current
        self.back_stack.push(self.current)
        self.current = self.forward_stack.pop()
        return self.current

    def current_page(self):
        return self.current


b = Browser()
b.visit("Google")
b.visit("YouTube")
b.visit("GitHub")
print("Back ->", b.back())
print("Back ->", b.back())
print("Forward ->", b.forward())
print("Current page:", b.current_page())
