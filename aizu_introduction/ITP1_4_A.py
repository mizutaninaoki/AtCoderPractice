# 3 2

# 1 1 1.50000

a, b = map(int, input().split())

d = a // b
r = a % b
f = a / b

# 小数第5位まで表示
print(d, r, format(f, ".5f"))


