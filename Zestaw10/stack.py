class Stack:
    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise OverflowError("The stack is full")
        else:
            self.items[self.n] = data
            self.n += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("The stack is empty")
        else:
            self.n -= 1
            data = self.items[self.n]
            self.items[self.n] = None    # usuwam referencję
            return data
