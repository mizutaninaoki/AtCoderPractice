from unittest import TestCase
from lessons.L08_equi_leader import solution


class EquiLeaderTest(TestCase):
    def test_sample(self):
        result = solution([4, 3, 4, 4, 4, 2])
        expect = 2
        self.assertEqual(expect, result)
