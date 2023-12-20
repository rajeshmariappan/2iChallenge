"""
Tests for the pairs module.
"""

import unittest
from pairs import find_pairing_sum

class TestPairs(unittest.TestCase):
    """
    Test pairs module.
    """
    def test_find_pairing_sum(self):
        """
        Test find_pairing_sum function.
        """
        self.assertEquals(find_pairing_sum([3, 4, 5, 6], 1), 0)
        self.assertEquals(find_pairing_sum([0, 15, 32, 2000, 15000], 15), 1)
        self.assertEquals(find_pairing_sum([1, 1, 10, 32, 41], 42), 2)
        self.assertEquals(find_pairing_sum([1, 2, 3, 4, 5, 6, 5, 4], 8), 3)


if __name__ == '__main__':
    unittest.main()
