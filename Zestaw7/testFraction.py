import fracs
import unittest


class TestFrac(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):
        self.assertEqual(str(fracs.Frac(2,3)), "2/3")
        self.assertEqual(repr(fracs.Frac(2,3)),"Frac(2,3)")

    def test_cmp_frac(self):
        self.assertTrue(fracs.Frac(1, 5) == fracs.Frac(1, 5))
        self.assertFalse(fracs.Frac(1, 3) == fracs.Frac(1, 6))

        self.assertTrue(fracs.Frac(1, 5) != fracs.Frac(1, 3))
        self.assertFalse(fracs.Frac(4, 3) != fracs.Frac(4, 3))

        self.assertFalse(fracs.Frac(2, 3) < fracs.Frac(1, 3))
        self.assertTrue(fracs.Frac(1, 4) < fracs.Frac(1, 2))

        self.assertTrue(fracs.Frac(1, 3) <= fracs.Frac(1, 3))
        self.assertFalse(fracs.Frac(1, 4) <= fracs.Frac(1, 6))

        self.assertTrue(fracs.Frac(4, 5) > fracs.Frac(1, 5))
        self.assertFalse(fracs.Frac(1, 4) > fracs.Frac(1, 2))

        self.assertTrue(fracs.Frac(3, 4) >= fracs.Frac(3, 4))
        self.assertFalse(fracs.Frac(3, 5) >= fracs.Frac(4, 5))



    def test_add(self):
        self.assertEqual(fracs.Frac(1, 2) + fracs.Frac(1, 4), fracs.Frac(3, 4))
        self.assertEqual(fracs.Frac(1, 3) + 4, fracs.Frac(13, 3))
        self.assertEqual(2 + fracs.Frac(1, 2), fracs.Frac(5, 2))
        self.assertEqual(fracs.Frac(1, 2) + 0.25, fracs.Frac(3, 4))

    def test_sub(self):
        self.assertEqual(fracs.Frac(1, 2) - 1.5, fracs.Frac(-1, 1))
        self.assertEqual(fracs.Frac(1, 2) - 1, fracs.Frac(-1, 2))
        self.assertEqual(fracs.Frac(1, 2) - fracs.Frac(1, 2), fracs.Frac(0, 1))
        self.assertEqual(2 - fracs.Frac(1, 2), fracs.Frac(3, 2))

    def test_mult(self):
        self.assertEqual(fracs.Frac(1, 2) * 1.5, fracs.Frac(3, 4))
        self.assertEqual(fracs.Frac(1, 2) * 2, fracs.Frac(1, 1))
        self.assertEqual(fracs.Frac(1, 2) * fracs.Frac(1, 2), fracs.Frac(1, 4))
        self.assertEqual(2 * fracs.Frac(1, 2), fracs.Frac(1, 1))

    def test_truediv(self):
        self.assertEqual(fracs.Frac(4, 5) / 2, fracs.Frac(2, 5))
        self.assertEqual(fracs.Frac(1, 8) / 2, fracs.Frac(1, 16))
        self.assertEqual(fracs.Frac(2, 1) / 1.25, fracs.Frac(8, 5))

    def test_pos(self):
        self.assertEqual(+fracs.Frac(-2, 3), fracs.Frac(-2, 3))
        self.assertEqual(+fracs.Frac(1, 2), fracs.Frac(1, 2))

    def test_invert(self):
        self.assertEqual(~fracs.Frac(2, 3), fracs.Frac(3, 2))
        self.assertEqual(~fracs.Frac(1, 2), fracs.Frac(2, 1))

    def test_float(self):
        self.assertEqual(float(fracs.Frac(1, 4)), 0.25)
        self.assertEqual(float(fracs.Frac(1, 2)), 0.5)


if __name__ == '__main__':
    unittest.main()
