from unittest import TestCase
from lessons.L02_cycle_rotation import solution


class CyclicRotationTest(TestCase):
    def test_sample(self):
        result = solution([3, 8, 9, 7, 6], 3)
        expect = [9, 7, 6, 3, 8]
        self.assertEqual(result, expect)

    def test_sample_zero_array(self):
        result = solution([0, 0, 0], 1)
        expect = [0, 0, 0]
        self.assertEqual(result, expect)

    def test_sample_not_change(self):
        result = solution([1, 2, 3, 4], 4)
        expect = [1, 2, 3, 4]
        self.assertEqual(result, expect)
