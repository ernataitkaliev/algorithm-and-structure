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


# Task 5 - Stack-Based Number Conversion (decimal -> binary)
def to_binary(number):
    if number == 0:
        return "0"
    st = Stack()
    while number > 0:
        st.push(number % 2)   # остаток от деления на 2
        number //= 2
    result = ""
    while not st.is_empty():
        result += str(st.pop())   # остатки читаем в обратном порядке
    return result


print("Input: 25  Output:", to_binary(25))
