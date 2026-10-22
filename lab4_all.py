# ============================================================
# LAB 4 - Stacks and Queues
# ============================================================


# ============================================================
# BASE CLASSES (used by the tasks below)
# ============================================================


# Stack - LIFO (Last In, First Out)
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


# Queue - FIFO (First In, First Out)
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


# ============================================================
# Task 1 - Implement a Stack: push, pop, peek, isEmpty, size (тест на 10 элементах)
# ============================================================
print("\n=== Task 1 ===")
s = Stack()
for i in range(1, 11):
    s.push(i * 10)

print("Stack:", s.items)
print("Size =", s.size())
print("Peek =", s.peek())
print("Pop =", s.pop())
print("Pop =", s.pop())
print("Size after 2 pops =", s.size())
print("Is empty =", s.is_empty())


# ============================================================
# Task 2 - Reverse a String Using a Stack
# ============================================================
print("\n=== Task 2 ===")
def reverse_string(text):
    st = Stack()
    for ch in text:
        st.push(ch)          # кладём буквы по порядку
    result = ""
    while not st.is_empty():
        result += st.pop()   # достаём в обратном порядке
    return result


print('Input: "HELLO"  Output:', reverse_string("HELLO"))


# ============================================================
# Task 3 - Check Balanced Parentheses
# ============================================================
print("\n=== Task 3 ===")
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


# ============================================================
# Task 4 - Remove Adjacent Duplicates
# ============================================================
print("\n=== Task 4 ===")
def remove_adjacent_duplicates(text):
    st = Stack()
    for ch in text:
        if not st.is_empty() and st.peek() == ch:
            st.pop()         # такая же буква сверху - удаляем пару
        else:
            st.push(ch)
    return "".join(st.items)


print('Input: "abbaca"  Output:', remove_adjacent_duplicates("abbaca"))


# ============================================================
# Task 5 - Stack-Based Number Conversion (decimal -> binary)
# ============================================================
print("\n=== Task 5 ===")
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


# ============================================================
# Task 6 - Implement a Queue: enqueue, dequeue, front, isEmpty, size (FIFO)
# ============================================================
print("\n=== Task 6 ===")
q = Queue()
for v in [1, 2, 3, 4, 5]:
    q.enqueue(v)

print("Queue:", q.items)
print("Front =", q.front())
print("Size =", q.size())

print("Dequeue order (FIFO):", end=" ")
while not q.is_empty():
    print(q.dequeue(), end=" ")
print()
print("Is empty =", q.is_empty())


# ============================================================
# Task 7 - Reverse a Queue Using a Stack
# ============================================================
print("\n=== Task 7 ===")
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


# ============================================================
# Task 8 - Generate Binary Numbers Using a Queue
# ============================================================
print("\n=== Task 8 ===")
def generate_binary(n):
    result = []
    q = Queue()
    q.enqueue("1")
    for i in range(n):
        current = q.dequeue()
        result.append(current)
        q.enqueue(current + "0")
        q.enqueue(current + "1")
    return result


N = 5
for b in generate_binary(N):
    print(b)


# ============================================================
# Task 9 - Evaluate a Postfix Expression
# ============================================================
print("\n=== Task 9 ===")
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


# ============================================================
# Task 10 - Infix to Postfix Conversion (+ - * / and parentheses)
# ============================================================
print("\n=== Task 10 ===")
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


# ============================================================
# Task 11 - Implement a Queue Using Two Stacks
# ============================================================
print("\n=== Task 11 ===")
class QueueTwoStacks:
    def __init__(self):
        self.in_stack = Stack()    # сюда добавляем
        self.out_stack = Stack()   # отсюда достаём

    def enqueue(self, value):
        self.in_stack.push(value)

    def _move(self):
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())

    def dequeue(self):
        self._move()
        return self.out_stack.pop()

    def peek(self):
        self._move()
        return self.out_stack.peek()

    def is_empty(self):
        return self.in_stack.is_empty() and self.out_stack.is_empty()


q = QueueTwoStacks()
for v in [1, 2, 3]:
    q.enqueue(v)
print("Dequeue:", q.dequeue())     # 1
q.enqueue(4)
print("Peek:", q.peek())           # 2
print("Dequeue:", q.dequeue(), q.dequeue(), q.dequeue())   # 2 3 4
print("Is empty:", q.is_empty())

# Почему это FIFO: при переносе из in_stack в out_stack порядок переворачивается,
# и самый старый элемент оказывается сверху out_stack - он и выходит первым.


# ============================================================
# Task 12 - Implement a Stack Using Two Queues
# ============================================================
print("\n=== Task 12 ===")
class StackTwoQueues:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, value):
        self.q2.enqueue(value)                 # новый элемент в пустую очередь
        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.dequeue()) # затем все старые за ним
        self.q1, self.q2 = self.q2, self.q1    # меняем очереди местами

    def pop(self):
        return self.q1.dequeue()

    def peek(self):
        return self.q1.front()

    def is_empty(self):
        return self.q1.is_empty()


s = StackTwoQueues()
for v in [1, 2, 3]:
    s.push(v)
print("Peek:", s.peek())                       # 3
print("Pop:", s.pop(), s.pop(), s.pop())       # 3 2 1 (LIFO)
print("Is empty:", s.is_empty())


# ============================================================
# Task 13 - Browser History Simulation
# ============================================================
print("\n=== Task 13 ===")
class Browser:
    def __init__(self):
        self.back_stack = Stack()
        self.forward_stack = Stack()
        self.current = None

    def visit(self, page):
        if self.current is not None:
            self.back_stack.push(self.current)
        self.current = page
        self.forward_stack = Stack()    # после нового visit "вперёд" очищается
        print("Visit:", page)

    def back(self):
        if self.back_stack.is_empty():
            return self.current
        self.forward_stack.push(self.current)
        self.current = self.back_stack.pop()
        return self.current

    def forward(self):
        if self.forward_stack.is_empty():
            return self.current
        self.back_stack.push(self.current)
        self.current = self.forward_stack.pop()
        return self.current

    def current_page(self):
        return self.current


b = Browser()
b.visit("Google")
b.visit("YouTube")
b.visit("GitHub")
print("Back ->", b.back())
print("Back ->", b.back())
print("Forward ->", b.forward())
print("Current page:", b.current_page())


# ============================================================
# Task 14 - CPU / Printer Task Scheduler (FIFO)
# ============================================================
print("\n=== Task 14 ===")
printer = Queue()
printer.enqueue((1, "Aigerim", 5))   # (Task ID, student name, pages)
printer.enqueue((2, "Dana", 2))
printer.enqueue((3, "Erlan", 8))

total_pages = 0
print("Processing order:")
while not printer.is_empty():
    task_id, name, pages = printer.dequeue()
    print("Task", task_id, "-", name, "->", pages, "pages")
    total_pages += pages

print("Total pages printed:", total_pages)


# ============================================================
# Task 15 - Undo/Redo System (two stacks)
# ============================================================
print("\n=== Task 15 ===")
class Editor:
    def __init__(self):
        self.text = ""
        self.undo_stack = Stack()
        self.redo_stack = Stack()

    def write(self, new_text):
        self.undo_stack.push(self.text)   # запоминаем текст до изменения
        self.redo_stack = Stack()         # новое действие очищает redo
        self.text += new_text

    def undo(self):
        if self.undo_stack.is_empty():
            return
        self.redo_stack.push(self.text)
        self.text = self.undo_stack.pop()

    def redo(self):
        if self.redo_stack.is_empty():
            return
        self.undo_stack.push(self.text)
        self.text = self.redo_stack.pop()

    def show_text(self):
        print("Text:", self.text)


ed = Editor()
ed.write("Hello")
ed.write(" World")
ed.show_text()    # Hello World
ed.undo()
ed.show_text()    # Hello
ed.redo()
ed.show_text()    # Hello World
ed.undo()
ed.undo()
ed.show_text()    # (пусто)
ed.redo()
ed.redo()
ed.show_text()    # Hello World
