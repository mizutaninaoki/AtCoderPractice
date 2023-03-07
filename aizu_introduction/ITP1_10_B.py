# 4 3 90

# 6.00000000
# 12.00000000
# 3.00000000

import math

a, b, c = map(float, input().split())

theta = math.radians(c)
h = b*math.sin(theta)
S = a*h/2

# 三角形の辺を求める公式の一つ
# 公式： a2=b**2+c**2−2bccosA
c = math.sqrt(a**2+b**2-2*a*b*math.cos(theta))
L = a+b+c

print(S)
print(L)
print(h)