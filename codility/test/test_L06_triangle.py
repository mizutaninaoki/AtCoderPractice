from unittest import TestCase
from lessons.L06_triangle import solution


class TriangleTest(TestCase):
    def test_sample_true(self):
        result = solution([10, 2, 5, 1, 8, 20])
        expect = 1
        self.assertEqual(expect, result)

    def test_sample_false(self):
        result = solution([10, 50, 5, 1])
        expect = 0
        self.assertEqual(expect, result)
