# 4
# 20 18 2 18

# #-----------------------
# # 自分の解法
# #-----------------------
# n = int(input())

# nums = list(map(int, input().split()))

# Alice = []
# Bob = []

# AliceTurn = True

# while True:
#     maxNum = max(nums)
#     if AliceTurn:
#         Alice.append(maxNum)
#         AliceTurn = False
#     else:
#         Bob.append(maxNum)
#         AliceTurn = True

#     nums.remove(maxNum)

#     if len(nums) == 0:
#         break

# print(sum(Alice) - sum(Bob))


#-----------------------
# お手本
#-----------------------
N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
alice = A[::2]
bob = A[1::2]

print(sum(alice) - sum(bob))