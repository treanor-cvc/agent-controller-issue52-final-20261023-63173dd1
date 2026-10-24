import unittest
from app import add


class AddTests(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_mixed_signs(self):
        for a, b, expected in [(5, -3, 2), (-3, 5, 2),
                               (3, -5, -2), (-5, 3, -2),
                               (4, -4, 0)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(add(a, b), expected)

    def test_zero(self):
        self.assertEqual(add(0, 0), 0)
        for value in (7, -7):
            with self.subTest(value=value):
                self.assertEqual(add(value, 0), value)
                self.assertEqual(add(0, value), value)


if __name__ == "__main__":
    unittest.main()
