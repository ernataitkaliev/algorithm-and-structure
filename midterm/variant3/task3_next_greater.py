# Variant 3 - Task 3. Stacks - Next Greater Element
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

def next_greater(arr):
    result = [-1] * len(arr)
    st = Stack()
    for i, x in enumerate(arr):
        while not st.is_empty() and arr[st.peek()] < x:
            result[st.pop()] = x
        st.push(i)
    return result

print([4, 5, 2, 10, 8], "->", next_greater([4, 5, 2, 10, 8]))
