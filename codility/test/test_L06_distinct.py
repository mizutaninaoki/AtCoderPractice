from unittest import TestCase
from codes.L06_Distinct import solution


class DistinctTest(TestCase):
    def test_sample(self):
        result = solution([2, 1, 1, 2, 3, 1])
        expect = 3
        self.assertEqual(expect, result)
