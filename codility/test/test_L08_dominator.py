from unittest import TestCase
from lessons.L08_dominator import solution


class DominatorTest(TestCase):
    def test_sample(self):
        result = solution([3, 4, 3, 2, 3, -1, 3, 3])
        expect = 0
        self.assertEqual(expect, result)

    def test_sample_last_def(self):
        result = solution([3, 4, 3, 2, 3, -1, 3, 3, 2])
        expect = 0
        self.assertEqual(expect, result)

    def test_sample_not_half(self):
        result = solution([3, 4, 3, 2, 3, -1, 2])
        expect = -1
        self.assertEqual(expect, result)

    def test_sample_not_half_2(self):
        result = solution([2, 1, 1, 3])
        expect = -1
        self.assertEqual(expect, result)
