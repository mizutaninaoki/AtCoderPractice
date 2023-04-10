# see: https://leetcode.com/problems/fibonacci-number/description/
# フィボナッチ数列のコード
class Solution:
    def fib(self, N: int) -> int:
        a, b = 0, 1
        for _ in range(N):
            a, b = b, a + b
        return a


# see: https://leetcode.com/problems/climbing-stairs/
# フィボナッチ数列
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        num1, num2 = 0, 1
        for i in range(n):
            num1, num2 = num2, num1+num2
        return num2
