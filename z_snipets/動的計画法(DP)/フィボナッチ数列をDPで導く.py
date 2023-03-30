# DPを使った解き方
# https://leetcode.com/problems/climbing-stairs/solutions/1531764/python-detail-explanation-3-solutions-easy-to-difficult-recursion-dictionary-dp/?orderBy=most_votes&languageTags=python
def climb(n):
    # edge cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    dp = [0]*(n+1)  # considering zero steps we need n+1 places
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp)
    return dp[n]
