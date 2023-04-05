from unittest import TestCase
from lessons.L03_tape_equilibrium import solution


class TapeEquilibrium(TestCase):
    def test_sample(self):
        result = solution([3, 1, 2, 4, 3])
        expect = 1
        self.assertEqual(expect, result)

    def test_two_number(self):
        result = solution([1, 2])
        expect = 1
        self.assertEqual(expect, result)

    def test_two_same_number(self):
        result = solution([2, 2])
        expect = 0
        self.assertEqual(expect, result)

    def test_two_max(self):
        result = solution([-1000, 1000])
        expect = 2000
        self.assertEqual(expect, result)
