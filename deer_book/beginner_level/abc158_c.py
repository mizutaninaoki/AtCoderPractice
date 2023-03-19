import math
a, b = map(int, input().split())

ans = -1
# bは100以下。つまり、価格はその10倍が最大値。よって1001にrangeの幅を設定する
for i in range(1, 1001):
    if math.floor(i * 0.08) == a and math.floor(i * 0.1) == b:
        ans = i
        break

print(ans)
