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


# Task 3 - Check Balanced Parentheses
def is_balanced(expr):
    st = Stack()
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in expr:
        if ch in "([{":
            st.push(ch)                              # открывающую кладём в стек
        elif ch in ")]}":
            if st.is_empty() or st.pop() != pairs[ch]:
                return False                         # нет пары или не та скобка
    return st.is_empty()                             # в конце стек должен быть пуст


for e in ["{[()]}", "{[(])}", "((", "())"]:
    print(e, "->", "Balanced" if is_balanced(e) else "Not balanced")
