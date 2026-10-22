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


# Task 15 - Undo/Redo System (two stacks)
class Editor:
    def __init__(self):
        self.text = ""
        self.undo_stack = Stack()
        self.redo_stack = Stack()

    def write(self, new_text):
        self.undo_stack.push(self.text)   # запоминаем текст до изменения
        self.redo_stack = Stack()         # новое действие очищает redo
        self.text += new_text

    def undo(self):
        if self.undo_stack.is_empty():
            return
        self.redo_stack.push(self.text)
        self.text = self.undo_stack.pop()

    def redo(self):
        if self.redo_stack.is_empty():
            return
        self.undo_stack.push(self.text)
        self.text = self.redo_stack.pop()

    def show_text(self):
        print("Text:", self.text)


ed = Editor()
ed.write("Hello")
ed.write(" World")
ed.show_text()    # Hello World
ed.undo()
ed.show_text()    # Hello
ed.redo()
ed.show_text()    # Hello World
ed.undo()
ed.undo()
ed.show_text()    # (пусто)
ed.redo()
ed.redo()
ed.show_text()    # Hello World
