from unittest import TestCase
from lessons.L06_max_product_of_three import solution


class MaxProductOfThreeTest(TestCase):
    def test_sample(self):
        result = solution([-3, 1, 2, -2, 5, 6])
        expect = 60
        self.assertEqual(expect, result)

    def test_pppp(self):
        result = solution([2, 4, 1, 3])
        expect = 24
        self.assertEqual(expect, result)

    def test_zppp(self):
        result = solution([0, 4, 1, 3])
        expect = 12
        self.assertEqual(expect, result)

    def test_nppp(self):
        result = solution([2, 4, -1, 3])
        expect = 24
        self.assertEqual(expect, result)

    def test_nnpp(self):
        result = solution([2, -4, 1, -3])
        expect = 24
        self.assertEqual(expect, result)

    def test_nzpp(self):
        result = solution([0, 4, 1, -3])
        expect = 0
        self.assertEqual(expect, result)

    def test_nnnp(self):
        result = solution([-2, 4, -1, -3])
        expect = 24
        self.assertEqual(expect, result)

    def test_nnzp(self):
        result = solution([-2, 4, 0, -3])
        expect = 24
        self.assertEqual(expect, result)

    def test_nnnz(self):
        result = solution([-2, -4, 0, -3])
        expect = 0
        self.assertEqual(expect, result)

    def test_nnnn(self):
        result = solution([-2, -4, -1, -3])
        expect = -6
        self.assertEqual(expect, result)