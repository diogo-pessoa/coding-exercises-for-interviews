from unittest import TestCase

from codility.primeComposite_nums.min_perimeter_rectangle import solution


class TestMinPerimeterRectangle(TestCase):
    def test_solution(self):
        A = 30
        self.assertEqual(22, solution(A))
