from unittest import TestCase
from lessons.L04_perm_check import solution


class PermCheckTest(TestCase):
    def test_sample(self):
        result = solution([4, 1, 3, 2])
        expect = 1
        self.assertEqual(expect, result)

    def test_sample_false(self):
        result = solution([4, 1, 3])
        expect = 0
        self.assertEqual(expect, result)

    def test_one_true(self):
        result = solution([1])
        expect = 1
        self.assertEqual(expect, result)

    def test_one_false(self):
        result = solution([2])
        expect = 0
        self.assertEqual(expect, result)
