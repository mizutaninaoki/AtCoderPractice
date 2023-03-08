# 9 45000

# 4 0 5


#
# 自分の解けなかった解法
#

# n, p = map(int, input().split())

# ichimanen = 0
# gosenen = 0
# senen = 0

# count = 0


# while True:
#     if p == 0: break

#     if p // 10000 > 0:
#         p -= 1000
#         ichimanen += 1
#         count += 1
#     else:
#         break

# while True:
#     if p == 0: break

#     if p // 5000 > 0:
#         p -= 1000
#         gosenen += 1
#         count += 1
#     else:
#         break

# while True:
#     if p == 0: break

#     if p // 1000 > 0:
#         p -= 1000
#         senen += 1
#         count += 1
#     else:
#         break

# if (p == 0) and (count <= n):
#     print(f"{ichimanen} {gosenen} {senen}")
# else:
#     print("-1 -1 -1")


#
# 解法
#
n, y = map(int, input().split())

for i in range(0, n+1):
    for j in range(0, n+1-i):
        if (n-i-j)*10000 + j*5000 + i*1000 == y:
            print(n-i-j, j, i)
            exit()

print(-1, -1, -1)