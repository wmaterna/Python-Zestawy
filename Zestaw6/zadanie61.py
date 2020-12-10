import unittest
import times

class TestTime(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):
        self.assertEqual(str(times.Time(2)), "00:00:02")
        self.assertEqual(str(times.Time(63)), "00:01:03")
        self.assertEqual(str(times.Time(3604)), "01:00:04")
        self.assertEqual(repr(times.Time(2)), "Time(2)")
        self.assertEqual(repr(times.Time(63)), "Time(63)")
        self.assertEqual(repr(times.Time(3604)), "Time(3604)")

    def test_add(self):
        self.assertEqual(times.Time(10) + times.Time(10), times.Time(20))
        self.assertEqual(times.Time(0) + times.Time(15), times.Time(15))
        self.assertEqual(times.Time(60) + times.Time(10), times.Time(70))

    def test_cmp(self):
        self.assertTrue(times.Time(1) == times.Time(1))
        self.assertTrue(times.Time(1) != times.Time(2))
        self.assertTrue(times.Time(3) > times.Time(2))
        self.assertTrue(times.Time(2) < times.Time(3))
        self.assertTrue(times.Time(2) >= times.Time(2))
        self.assertTrue(times.Time(3) >= times.Time(2))

    def test_int(self):
        self.assertEqual(int(times.Time(1.5)), 1)

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()  # wszystkie testy
