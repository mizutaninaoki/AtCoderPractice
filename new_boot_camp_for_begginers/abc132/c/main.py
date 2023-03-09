# 6
# 9 1 4 4 6 7

# 2


n = int(input())
l = sorted(list(map(int, input().split())))

half = len(l) // 2

# 偶数nの真ん中２つの数が同じ場合は、K=0になる
if l[half] == l[half - 1]:
    print(0)
    exit()

# 偶数nの真ん中２つの数の差の数だけK個の境界線を作れる
print(l[half] - l[half - 1])
