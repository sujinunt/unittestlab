import unittest

from listutil import count_unique

class Testing(unittest.TestCase):
    """Test count_unique function in Python. """
    def test_borderline(self):
        """Test a list with 0 element."""
        self.assertEqual(count_unique([]), 0)
    def test_typical(self):
        """Test a few duplicates in list."""
        self.assertEqual(count_unique(["a","b","a"]), 2)
    def test_impossible(self):
        """Test an impossible case."""
        with self.assertRaises(Exception): count_unique()
    def test_extreme(self):
        """Test huge list."""
        self.assertEqual(count_unique(['a','b','b','b','a','c','c','d','d','d','f','e']), 6)


if __name__ == '__main__':
    unittest.main()