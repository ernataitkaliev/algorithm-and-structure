# Variant 2 - Task 3. Stacks - Evaluate a Postfix Expression
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

def divide_truncate(a, b):
    q = abs(a) // abs(b)
    if (a < 0) != (b < 0):
        q = -q
    return q

def evaluate_postfix(expr):
    st = Stack()
    for token in expr.split():
        if token in ("+", "-", "*", "/"):
            b = st.pop()
            a = st.pop()
            if token == "+":
                st.push(a + b)
            elif token == "-":
                st.push(a - b)
            elif token == "*":
                st.push(a * b)
            else:
                st.push(divide_truncate(a, b))
        else:
            st.push(int(token))
    return st.pop()

print('"12 3 4 * +" ->', evaluate_postfix("12 3 4 * +"))
print('"7 2 /"      ->', evaluate_postfix("7 2 /"))
print('"2 7 - 3 /"  ->', evaluate_postfix("2 7 - 3 /"))
