class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie



class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0   # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def __str__(self):
        list = ''
        node = self.head
        while node != None:
            list = list + (',' + str(node))
            node = node.next
        list = '{' + list[1:] + '}'
        return list

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):  # klasy O(n)
        if self.head:  # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1


    def remove_head(self):          # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node

    def remove_tail(self):
        # Zwraca cały węzeł, skraca listę.
        # Dla pustej listy rzuca wyjątek ValueError.
        if self.is_empty():
            raise ValueError("Empty list")
        elif self.head == self.tail:
            node = self.tail
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            node = self.head
            while node.next != self.tail:
                node = node.next
            nodeToReturn = node.next
            node.next = None
            self.tail = node
            return nodeToReturn



    def merge(self, other):
        # Węzły z listy other są przepinane do listy self na jej koniec.
        # Po zakończeniu operacji lista other ma być pusta.

        if other.head:
            self.tail.next = other.head
            self.tail = other.tail
            self.length = self.length + other.length

            other.length = 0
            other.head = None
            other.tail = None


    def clear(self): # czyszczenie listy
        self.head = None
        self.tail = None
        self.length = 0




print("Lista A")
alist = SingleList()

alist.insert_head(Node(11))         # [11]
alist.insert_head(Node(22))         # [22, 11]
alist.insert_tail(Node(33))         # [22, 11, 33]
print ( "length {}".format(alist.length) ) # odczyt atrybutu
print("wnetrze listy")
print(alist)
print("Lista B")
blist = SingleList()
blist.insert_head(Node(2))
blist.insert_head(Node(1))
print ( "length {}".format(blist.length) ) # odczyt atrybutu
print("wnetrze listy")
print(blist)



print("MERGE")
alist.merge(blist)
print("listy po merge")
print(alist)
print(blist)
print ( "length {}".format(alist.length) )
print ( "length {}".format(blist.length) )
print("CLEAR")
alist.clear()
print ( "length {}".format(alist.length) )
print ( "length {}".format(blist.length) )
print(alist)
print(blist)