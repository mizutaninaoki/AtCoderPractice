from unittest import TestCase
from lessons.L04_frog_river_one import solution


class FrogRiverOneTest(TestCase):
    def test_sample(self):
        result = solution(5, [1, 3, 1, 4, 2, 3, 5, 4])
        expect = 6
        self.assertEqual(expect, result)

    def test_only_one(self):
        result = solution(1, [1])
        expect = 0
        self.assertEqual(expect, result)