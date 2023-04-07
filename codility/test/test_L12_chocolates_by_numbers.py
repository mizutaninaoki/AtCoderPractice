from unittest import TestCase
from lessons.L12_chocolates_by_numbers import solution


class ChocolatesByNumbersTest(TestCase):
    def test_sample(self):
        result = solution(10, 4)
        expect = 5
        self.assertEqual(expect, result)
