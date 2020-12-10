import rectangles
import unittest
from points import Point


class TestFrac(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):
        self.assertEqual(str(rectangles.Rectangle(0, 0, 8, 4)), "[(0, 0), (8, 4)]")
        self.assertEqual(repr(rectangles.Rectangle(0, 0, 8, 4)), "Rectangle(0,0,8,4)")

    def test_cmp_rect(self):
        self.assertTrue(rectangles.Rectangle(0, 0, 8, 4) == rectangles.Rectangle(0, 0, 8, 4))

    def test_center(self):
        self.assertEqual(rectangles.Rectangle(1,1,3,3).center(), Point(2,2))

    def test_move(self):
        self.assertEqual(rectangles.Rectangle(1, 1, 3, 3).move(1,1), rectangles.Rectangle(2,2,4,4))

    def test_intersection(self):
        self.assertEqual(rectangles.Rectangle(1, 1, 5, 3).intersection(rectangles.Rectangle(3, 1, 5, 2)),rectangles.Rectangle(3, 1, 5, 2))

    def test_cover(self):
        self.assertEqual(rectangles.Rectangle(1, 1, 5, 3).cover(rectangles.Rectangle(3, 0, 7, 2)),rectangles.Rectangle(1, 0, 7, 3))


    def test_make4(self):
        self.assertEqual(rectangles.Rectangle(1, 1, 5, 3).make4(), [rectangles.Rectangle(1, 1, 3, 2),rectangles.Rectangle(3, 2, 5, 3),rectangles.Rectangle(1, 2, 3, 3),rectangles.Rectangle(3, 1, 5, 2)])


if __name__ == '__main__':
    unittest.main()