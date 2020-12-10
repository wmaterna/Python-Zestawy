import unittest
import points

class TestPoint(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):
        self.assertEqual(str(points.Point(2,3)),"(2,3)")
        self.assertEqual(str(points.Point(-1,3)), "(-1,3)")
        self.assertEqual(repr(points.Point(2,0)), "Point(2,0)")
        self.assertEqual(repr(points.Point(6,-3)), "Point(6,-3)")


    def test_add(self):
        self.assertEqual(points.Point(3, 2) + points.Point(-1, 0), points.Point(2, 2))
        self.assertEqual(points.Point(2, 5) + points.Point(0, 1), points.Point(2, 6))
        self.assertEqual(points.Point(8, 0) + points.Point(-2, 3), points.Point(6, 3))

    def test_sub(self):
        self.assertEqual(points.Point(3, -1) - points.Point(2, 2), points.Point(1, -3))
        self.assertEqual(points.Point(2, 5) - points.Point(-4, -1), points.Point(6, 6))

    def test_mul(self):
        self.assertEqual(points.Point(1, 2) * points.Point(3, -5), -7)
        self.assertEqual(points.Point(2, 1) * points.Point(-1, -1), -3)

    def test_cross(self):
        self.assertEqual(points.Point.cross(points.Point(2, 3), points.Point(4, -1)), -14)

    def test_length(self):
        self.assertEqual(points.Point.length(points.Point(3, 4)), 5)

    def test_cmp(self):
        self.assertTrue(points.Point(1, 2) == points.Point(1, 2))
        self.assertFalse(points.Point(3, 2) == points.Point(2, 3))
        self.assertTrue(points.Point(1, 2) != points.Point(2, 1))
        self.assertFalse(points.Point(8, -2) != points.Point(8, -2))





    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()