class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # @lru_cache(None)は再帰関数の時に使える、高速化するデコレーター。@lru_cache(None)がないとTLEになる。
        # see: https://qiita.com/KueharX/items/5a8993968c995b074737
        @lru_cache(None)
        def climb(n):
             if n == 1:  # only one step option is availble
                 return 1
             if n == 2:  # two options are possible : to take two 1-stpes or to only take one 2-steps
                 return 2
             return climb(n-1) + climb(n-2)
         return climb(n)


# フィボナッチ数列の解き方でもいける
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        num1, num2 = 0, 1
        for i in range(n):
            num1, num2 = num2, num1+num2
        return num2
    
    
# DPを使った解き方
def climb(n):
    #edge cases
    if n==0: return 0
    if n==1: return 1
    if n==2: return 2
    dp = [0]*(n+1) # considering zero steps we need n+1 places
    dp[1]= 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-1] +dp[i-2]
    print(dp)
    return dp[n]
		