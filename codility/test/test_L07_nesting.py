from unittest import TestCase
from lessons.L07_nesting import solution


class NestingTest(TestCase):
    def test_sample_true(self):
        result = solution('(()(())())')
        expect = 1
        self.assertEqual(expect, result)

    def test_sample_false(self):
        result = solution('())')
        expect = 0
        self.assertEqual(expect, result)

    def test_one_false_left(self):
        result = solution('())')
        expect = 0
        self.assertEqual(expect, result)

    def test_one_false_right(self):
        result = solution(')')
        expect = 0
        self.assertEqual(expect, result)
