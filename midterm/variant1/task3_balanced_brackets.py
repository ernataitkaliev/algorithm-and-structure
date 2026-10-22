# Variant 1 - Task 3. Stacks - Balanced Brackets
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def is_balanced(text):
    st = Stack()
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in text:
        if ch in "([{":
            st.push(ch)
        elif ch in ")]}":
            if st.is_empty() or st.pop() != pairs[ch]:
                return False
    return st.is_empty()

for expr in ("{[()]}", "{[(])}", "((", "())"):
    print('"' + expr + '" ->', is_balanced(expr))
