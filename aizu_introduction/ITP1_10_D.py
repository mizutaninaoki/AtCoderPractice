# 3
# 1 2 3
# 2 0 4

# 4.000000
# 2.449490
# 2.154435
# 2.000000

#---------------------
# 自分の解法
#---------------------
# import math

# n = int(input())
# x = list(map(int, input().split()))
# y = list(map(int, input().split()))


# # マンハッタン距離
# manhattan = 0
# for i in range(n):
#     manhattan += abs(x[i] - y[i])
# print(manhattan)

# # ユークリッド距離
# euclidean = 0
# for i in range(n):
#     euclidean += abs(x[i] - y[i])**2
# print(math.sqrt(euclidean))

# # p = 3の時
# p3 = 0
# for i in range(n):
#     p3 += abs(x[i] - y[i])**3
# print(p3**(1/3))

# # p = ∞の時
# l = []
# for i in range(n):
#     l.append(abs(x[i] - y[i]))
# print(max(l))



#---------------------
# きれいな解法
#---------------------
n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

print(sum([abs(x-y) for x,y in zip(x, y)]))
print(sum([abs(x-y)**2 for x,y in zip(x, y)]) ** (1/2))
print(sum([abs(x-y)**3 for x,y in zip(x, y)]) ** (1/3))
print(max([abs(x-y) for x,y in zip(x, y)]))

