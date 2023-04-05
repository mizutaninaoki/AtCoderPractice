from unittest import TestCase
from lessons.L03_frog_jmp import solution


class FrogJmpTest(TestCase):
    def test_sample(self):
        result = solution(10, 85, 30)
        expect = 3
        self.assertEqual(expect, result)
