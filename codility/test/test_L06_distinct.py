from unittest import TestCase
from lessons.L06_distinct import solution


class DistinctTest(TestCase):
    def test_sample(self):
        result = solution([2, 1, 1, 2, 3, 1])
        expect = 3
        self.assertEqual(expect, result)
