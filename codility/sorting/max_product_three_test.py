from unittest import TestCase

from codility.sorting.max_product_three import solution


class TestMaxProductThree(TestCase):
    def test_solution(self):
        self.assertEqual(60, solution([-3, 1, 2, -2, 5, 6]))
