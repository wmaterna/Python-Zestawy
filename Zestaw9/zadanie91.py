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
        if self.is_empty():
            raise ValueError("Empty list")
        node = self.head
        if self.head == self.tail: #jeden element w liscie
            self.head = self.tail = None
        else:
            n=0
            while  n != (self.length - 1):
                node = node.next
                n +=1
            node.next == None
            self.tail = node
            self.length -= 1

        return node



    def merge(self, other):
          if self.is_empty():
            self.head = self.tail = other.head
            self.length +=1
            other.length -= 1
          else:
              while other.length > 0:
                self.tail.next = other.head
                self.tail = other.head
                self.length += 1

                node = other.head
                if other.head == other.tail:
                      other.head = other.tail = None
                else:
                      other.head = other.head.next
                node.next = None
                other.length -= 1


    def clear(self):
        if self.is_empty():
            print("List is empty")
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            node = self.head
            while self.length > 1:
                node = node.next
                node.next == None
                self.tail = node
                self.length -= 1
            self.head = self.tail = None
            self.length = 0




print("Lista A")
alist = SingleList()
alist.insert_head(Node(11))         # [11]
alist.insert_head(Node(22))         # [22, 11]
alist.insert_tail(Node(33))         # [22, 11, 33]
print ( "length {}".format(alist.length) ) # odczyt atrybutu
print ( "length {}".format(alist.count()) ) # wykorzystujemy interfejs
print("Lista B")
blist = SingleList()
blist.insert_head(Node(11))         # [11]
blist.insert_head(Node(22))         # [22, 11]
blist.insert_tail(Node(33))         # [22, 11, 33]
print ( "length {}".format(blist.length) ) # odczyt atrybutu
print ( "length {}".format(blist.count()) ) # wykorzystujemy interfejs

print("MERGE")
alist.merge(blist)
print ( "length {}".format(alist.length) )
print ( "length {}".format(blist.length) )

alist.clear()


