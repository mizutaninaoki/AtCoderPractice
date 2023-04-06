from unittest import TestCase
from lessons.L07_stone_wall import solution


class StoneWallTest(TestCase):
    def test_sample(self):
        result = solution([8, 8, 5, 7, 9, 8, 7, 4, 8])
        expect = 7
        self.assertEqual(expect, result)
