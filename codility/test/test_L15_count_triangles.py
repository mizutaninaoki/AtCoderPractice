from unittest import TestCase
from lessons.L15_count_triangles import solution


class CountTrianglesTest(TestCase):
    def test_sample(self):
        result = solution([10, 2, 5, 1, 8, 12])
        expect = 4
        self.assertEqual(expect, result)
