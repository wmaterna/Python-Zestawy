import random

class RandomQueue:

    def __init__(self):
        self.items = []
        self.length = 0

    def __str__(self):
        return str(self.items)


    def insert(self, item):
        self.items.append(item)
        self.length +=1

    def remove(self):   # zwraca losowy element
        index = random.randint(0, self.length-1)
        removedElement = self.items[index]
        self.items[index], self.items[self.length-1] = self.items[self.length-1], self.items[index]
        del self.items[self.length-1]
        self.length = self.length - 1
        return removedElement

    def is_empty(self):
        return not self.items


    def is_full(self):
        return False #kolejka nigdy nie jest pusta

    def clear(self):
        self.items = []


randomQueue = RandomQueue()
randomQueue.insert(2)
randomQueue.insert(4)
randomQueue.insert(8)
randomQueue.insert(10)
print(randomQueue)
print(randomQueue.remove())
print(randomQueue)
print(randomQueue.remove())
print(randomQueue)
print(randomQueue.remove())
print(randomQueue)
randomQueue.insert(5)
randomQueue.insert(1)
print(randomQueue)
print("CLEAR")
randomQueue.clear()
print(randomQueue)


