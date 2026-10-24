import unittest
from app import add


class AddTests(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(add(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
