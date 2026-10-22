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


# Task 4 - Remove Adjacent Duplicates
def remove_adjacent_duplicates(text):
    st = Stack()
    for ch in text:
        if not st.is_empty() and st.peek() == ch:
            st.pop()         # такая же буква сверху - удаляем пару
        else:
            st.push(ch)
    return "".join(st.items)


print('Input: "abbaca"  Output:', remove_adjacent_duplicates("abbaca"))
