from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
    # Chcemy, aby x1 < x2, y1 < y2.
        if x1 >= x2 or y1 >= y2:
          raise ValueError("Złe dane: chcemy, aby x1 < x2, y1 < y2")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):        # "[(x1, y1), (x2, y2)]"
        return "[({}, {}), ({}, {})]".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)


    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle({},{},{},{})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)


    def __eq__(self, other):
        return self.pt1.x == other.pt1.x and self.pt2.x == self.pt2.x and self.pt1.y == other.pt1.y and self.pt2.y == self.pt2.y

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):           # zwraca środek prostokąta
        xCenter = (self.pt1.x + self.pt2.x) / 2
        yCenter = (self.pt1.y + self.pt2.y) / 2
        return Point(xCenter,yCenter)

    def area(self): # pole powierzchni
        a = self.pt2.x - self.pt1.x
        b = self.pt2.y - self.pt1.y
        return a * b


    def move(self, x, y):  # przesunięcie o (x, y)
        return Rectangle(self.pt1.x + x, self.pt1.y + y,self.pt2.x + x, self.pt2.y)

    def intersection(self, other): # część wspólna prostokątów

        x3 = max(self.pt1.x, other.pt1.x)
        y3 = max(self.pt1.y, other.pt1.y)
        x4 = min(self.pt2.x, other.pt2.x)
        y4 = min(self.pt2.y, other.pt2.y)
        return Rectangle(x3,y3,x4,y4)

    def cover(self, other):
        x3 = min(self.pt1.x, other.pt1.x)  # prostąkąt nakrywający oba
        y3 = min(self.pt1.y, other.pt1.y)
        x4 = max(self.pt2.x, other.pt2.x)
        y4 = max(self.pt2.y, other.pt2.y)
        return Rectangle(x3, y3, x4, y4)


    def make4(self):  # zwraca krotkę czterech mniejszych
        xCenter = (self.pt1.x + self.pt2.x) / 2
        yCenter = (self.pt1.y + self.pt2.y) / 2
        return [Rectangle(self.pt1.x,self.pt1.y, xCenter,yCenter),
                Rectangle(xCenter,yCenter,self.pt2.x,self.pt2.y),
                Rectangle(self.pt1.x, yCenter, xCenter,self.pt2.y),
                Rectangle(xCenter,self.pt1.y,self.pt2.x, yCenter)]