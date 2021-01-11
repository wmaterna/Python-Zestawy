from queue import *
import unittest


class QueueTest(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_str(self):
        self.assertEqual(str(self.queue), '[]')


    def test_is_empty(self):
        self.assertEqual(self.queue.is_empty(), True)

    def test_is_full(self):
        self.assertEqual(self.queue.is_full(), False)

    def test_get(self):
        self.queue.put(12)
        self.assertEqual(self.queue.get(), 12)

    def test_put(self):
        self.queue.put(5)
        self.queue.put(4)
        self.queue.put(3)
        self.queue.put(2)
        self.queue.put(1)
        self.assertEqual(str(self.queue), '[5, 4, 3, 2, 1]')



if __name__ == '__main__':
    unittest.main()
