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


# Task 9 - Evaluate a Postfix Expression
def evaluate_postfix(expr):
    st = Stack()
    for token in expr.split():
        if token in "+-*/":
            b = st.pop()     # второй операнд лежит сверху
            a = st.pop()
            if token == "+":
                st.push(a + b)
            elif token == "-":
                st.push(a - b)
            elif token == "*":
                st.push(a * b)
            else:
                st.push(a / b)
        else:
            st.push(int(token))
    return st.pop()


print("Input: 5 3 + 2 *  Output:", evaluate_postfix("5 3 + 2 *"))
print("Input: 2 3 4 * +  Output:", evaluate_postfix("2 3 4 * +"))
