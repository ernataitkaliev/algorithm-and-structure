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


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Task 7 - Reverse a Queue Using a Stack
def reverse_queue(queue):
    st = Stack()
    while not queue.is_empty():
        st.push(queue.dequeue())   # всё из очереди в стек
    while not st.is_empty():
        queue.enqueue(st.pop())    # из стека обратно в очередь
    return queue


q = Queue()
for v in [10, 20, 30, 40, 50]:
    q.enqueue(v)

print("Input: ", *q.items)
reverse_queue(q)
print("Output:", *q.items)
