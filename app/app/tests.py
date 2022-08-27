"""
Unit testing
"""

from django.test import SimpleTestCase
from app import calc


class Add_integers (SimpleTestCase):

    def test_addition(self):
        """Test number addition"""
        res = calc.add(9, 3)

        self.assertEqual(res, 12)

    def test_subtraction(self):
        """Test number subtraction"""
        res = calc.subtractNum(5, 10)

        self.assertEqual(res, 5)

    def test_distinct_vales(self):
        """Testing distinct values"""
        res = calc.distdistinct_val([1, 4, 3, 4, 3, 4, 5])

        self.assertEqual(res, [1, 3, 4, 5])
