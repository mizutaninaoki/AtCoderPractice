# 0 0 1 1

# 1.41421356


import math

x1, y1, x2, y2 = map(float, input().split())
print(math.hypot(x2-x1, y2-y1))
# math.distはpython3.8から追加されたメソッドのため、aizuでは使えなかった。
# print(math.dist((x1, y1), (x2, y2)))