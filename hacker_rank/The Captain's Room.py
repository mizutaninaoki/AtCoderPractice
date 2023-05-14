from collections import Counter

n = int(input())
l = list(map(int, input().split()))
for k, v in Counter(l).items():
    if v == 1:
        print(k)
        exit()