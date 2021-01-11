from stack import *
import unittest


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack(3)

    def test_str(self):
        self.assertEqual(str(self.stack), '[None, None, None]')

    def test_is_empty(self):
        self.assertEqual(self.stack.is_empty(), True)

    def test_is_full(self):
        self.assertEqual(self.stack.is_full(), False)

    def test_pop(self):
        self.stack.push(12)
        self.assertEqual(self.stack.pop(), 12)

    def test_push(self):
        self.stack.push(2)
        self.stack.push(9)
        self.stack.push(8)
        self.assertEqual(str(self.stack), '[2, 9, 8]')



if __name__ == '__main__':
    unittest.main()