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


# Task 2 - Reverse a String Using a Stack
def reverse_string(text):
    st = Stack()
    for ch in text:
        st.push(ch)          # кладём буквы по порядку
    result = ""
    while not st.is_empty():
        result += st.pop()   # достаём в обратном порядке
    return result


print('Input: "HELLO"  Output:', reverse_string("HELLO"))
