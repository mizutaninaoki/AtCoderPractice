# -------------------------------------------------------------------------------------------------------------------
# 再帰関数の例(これはフィボナッチ数列を解く、階段を一段、二段で進む場合、N段の時に何通りの進み方があるかを導く場合に使える)
# -------------------------------------------------------------------------------------------------------------------
# フィボナッチ数列を解く場合にも使える
class Solution(object):
    def climbStairs(self, n):
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