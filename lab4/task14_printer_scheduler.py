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


# Task 14 - CPU / Printer Task Scheduler (FIFO)
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
