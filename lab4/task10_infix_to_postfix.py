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


# Task 10 - Infix to Postfix Conversion (+ - * / and parentheses)
def infix_to_postfix(expr):
    priority = {"+": 1, "-": 1, "*": 2, "/": 2}
    st = Stack()
    output = []
    for ch in expr:
        if ch == " ":
            continue
        if ch.isalnum():
            output.append(ch)                 # операнд сразу в вывод
        elif ch == "(":
            st.push(ch)
        elif ch == ")":
            while not st.is_empty() and st.peek() != "(":
                output.append(st.pop())
            st.pop()                          # убираем "("
        else:
            while (not st.is_empty() and st.peek() != "("
                   and priority[st.peek()] >= priority[ch]):
                output.append(st.pop())
            st.push(ch)
    while not st.is_empty():
        output.append(st.pop())
    return " ".join(output)


print("A + B * C           ->", infix_to_postfix("A + B * C"))
print("(A + B) * C         ->", infix_to_postfix("(A + B) * C"))
print("A + B * C - D / E   ->", infix_to_postfix("A + B * C - D / E"))
