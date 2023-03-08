# 2
# 1 4

# 5
import statistics
# import math

n = int(input())
l = list(map(int, input().split()))

mean = round(statistics.mean(l))

p = 0

for i in l:
    p += (i - mean)**2

print(p)


# #----------------------------------------------------------
# # githubにあった回答の、全探索でPを求めるやり方の方が一般的っぽい
# #----------------------------------------------------------
# n = int(input())
# x = list(map(int, input().split()))
# ans = float('inf')
# mxi = min(x)
# mxa = max(x)
# for p in range(mxi, mxa+1):
#     sm = 0
#     for xi in x:
#         sm += (xi-p)**2
#     ans = min(ans, sm)
# print(ans)