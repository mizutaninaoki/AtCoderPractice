from unittest import TestCase
from lessons.L10_count_factors import solution


class CountFactorsTest(TestCase):
    def test_sample(self):
        result = solution(24)
        expect = 8
        self.assertEqual(expect, result)

    def test_sample_36(self):
        result = solution(36)
        expect = 9
        self.assertEqual(expect, result)
