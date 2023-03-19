#--------------------------
# 自分の解答(AC)
#--------------------------
# n, x = map(int, input().split())
# l = sorted([int(input()) for _ in range(n)])

# cnt = 0
# for i in l:
#     if x >= i:
#         x -= i
#         cnt += 1

# while x >= l[0]:
#     x -= l[0]
#     cnt += 1

# print(cnt)



#--------------------------
# 他者の解答の方がシンプル
#--------------------------
n, x = list(map(int, input().split()))
line =  [int(input()) for i in range(n)]
 
sum_l = sum(line)
min_l = min(line)
 
print( n + (x-sum_l) // min_l)