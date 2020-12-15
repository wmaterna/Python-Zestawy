class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def insert(self, node):
        if node.data < self.data:   # mniejsze na lewo
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
        else:   # większe lub równe na prawo
            if self.right:
                self.right.insert(node)
            else:
                self.right = node

    def count(self):
        counter = 1
        if self.left:
            counter += self.left.count()
        if self.right:
            counter += self.right.count()
        return counter

    def search(self, data):
        if self.data == data:
            return self
        if data < self.data:
            if self.left:
                return self.left.search(data)
        else:
            if self.right:
                return self.right.search(data)
        return None

    def remove(self, data):  # self na pewno istnieje
        # Są lepsze sposoby na usuwanie.
        if data < self.data:
            if self.left:
                self.left = self.left.remove(data)
        elif self.data < data:
            if self.right:
                self.right = self.right.remove(data)
        else:                # self.data == data
            if self.left is None:   # przeskakuje self
                return self.right
            else:     # self.left na pewno niepuste
                # Szukamy największego w lewym poddrzewie.
                node = self.left
                while node.right:   # schodzimy w dół
                    node = node.right
                node.right = self.right   # przyczepiamy
                return self.left
        return self

    def bst_max(top):
        while top.right is not None:
            top = top.right
        return top.data


    def bst_min(top):
        while top.left is not None:
            top = top.left
        return top.data


bst = Node(1)
bst.insert(Node(8))
bst.insert(Node(3))
bst.insert(Node(2))
bst.insert(Node(4))
bst.insert(Node(5))
bst.insert(Node(6))

print(bst.bst_max())
