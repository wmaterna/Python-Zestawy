class Time:
    """Klasa reprezentująca odcinek czasu."""

    def __init__(self, s=0):
        """Zwraca instancję klasy Time."""
        self.s = int(s)

    def __str__(self):
        """Zwraca string 'hh:mm:ss'."""
        h = self.s // 3600
        sec = self.s - h * 3600
        m = sec // 60
        sec = sec - m * 60
        return "{0:02d}:{1:02d}:{2:02d}".format(h, m, sec)

    def __repr__(self):
        """Zwraca string 'Time(s)'."""
        return "Time({0})".format(self.s)

    def __add__(self, other):
        """Dodawanie odcinków czasu."""
        return Time(self.s + other.s)

    #def __cmp__(self, other): # Python 2, porównywanie, -1|0|+1
    #    """Porównywanie odcinków czasu."""
    #    return cmp(self.s, other.s)

    # Python 2.7 i Python 3, rich comparisons.
    def __eq__(self, other):
        return self.s == other.s

    def __ne__(self, other):
        return self.s != other.s

    def __lt__(self, other):
        return self.s < other.s

    def __le__(self, other):
        return self.s <= other.s

    def __gt__(self, other):
        return self.s > other.s

    def __ge__(self, other):
        return self.s >= other.s

    def __int__(self):
        """Konwersja odcinka czasu do int."""
        return self.s
