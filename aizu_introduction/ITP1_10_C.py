# 5
# 70 80 100 90 20
# 3
# 80 80 80
# 0

# 27.85677655
# 0.00000000


import statistics
import math

while True:
    n = int(input())
    if n == 0: break

    l = list(map(int, input().split()))

    hensa = 0
    mean = statistics.mean(l)
    for i in l:
        # 「(期待値 - μ)**2 / n」-> 分散
        hensa += (i-mean)**2 / n

    print(math.sqrt(hensa))


