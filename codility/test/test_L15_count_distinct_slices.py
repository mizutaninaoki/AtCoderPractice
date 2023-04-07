from unittest import TestCase
from codes.L15_CountDistinctSlices import solution


class CountDistinctSlicesTest(TestCase):
    def test_sample(self):
        result = solution(6, [3, 4, 5, 5, 2])
        expect = 9
        self.assertEqual(expect, result)
