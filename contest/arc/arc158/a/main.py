# 4
# 2 8 8
# 1 1 1
# 5 5 10
# 10 100 1000

# 2
# 0
# -1
# 315

# --------------------------------------------------------------------
# 正解コード(https://atcoder.jp/contests/arc158/submissions/39684045)
# --------------------------------------------------------------------
T = int(input())
for _ in range(T):
  x1, x2, x3 = list(map(int, input().split()))
  if (x1+x2+x3) % 3 != 0 or not (x1 % 2 == x2 % 2 and x1 % 2 == x3 % 2):
    print(-1)
  else:
    a = (x1+x2+x3)//3
    d = abs(x1-a)+abs(x2-a)+abs(x3-a)
    print(d//4)


# t = int(input())

# for i in range(t):
#     x1, x2, x3 = map(int, input().split())

#     if x1 == x2 == x3:
#         print(0)
#         continue

#     # 全て奇数 or 偶数
#     if (x1 % 2) == (x2 % 2) == (x3 % 2):
#         can_divide = True
#         cnt = 0
#         while True:
#             minNum = min(x1, x2, x3)
#             maxNum = max(x1, x2, x3)
#             medNum = list(set([minNum, maxNum]) ^ set([x1, x2, x3]))

#             if medNum == []:
#                 medNum = list(set([minNum, maxNum]) & set([x1, x2, x3]))

#             medNum = medNum[0]

#             if can_divide:
#                 diff = maxNum - minNum
#                 div_count = diff // 7

#                 if div_count < 1:
#                     can_divide = False
#                     continue

#                 maxNum = (div_count * 3) + maxNum
#                 medNum = (div_count * 5) + medNum
#                 minNum = (div_count * 7) + minNum
#                 cnt += div_count
#             else:
#                 maxNum += 3
#                 medNum += 5
#                 minNum += 7
#                 cnt += 1

#             if minNum == medNum == maxNum:
#                 print(cnt)
#                 break

#             x1, x2, x3 = minNum, medNum, maxNum

#         continue

#     # ３つの数字の奇数、偶数が揃っていない
#     print(-1)
