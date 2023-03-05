# 2

# 12.566371 12.566371


import math

# 入力値は整数ではなく、「実数」であるため、floatで変換する
r = float(input())

a = format(r*r*math.pi, ".5f") # 面積 -> rの2乗×π
b = format(2*r*math.pi, ".5f") # 円周 -> 2πr

print(a, b)


