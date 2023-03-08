# 1 21

# Yes

import math

a, b = input().split()

s = a + b
num = int(s)
sq = int(math.sqrt(num))

if sq**2 == num:
    print('Yes')
else:
    print("No")


#---------------------
# 全探索でもいける
#---------------------
# import math
# a, b = input().split()
# ab = int(a+b)
# for i in range(1,1001):
#     if i**2==ab:
#         print('Yes')
#         exit()
# print('No')