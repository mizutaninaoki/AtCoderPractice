n = int(input())
l = sorted(list(map(int, input().split())))
print(l[(len(l) // 2)] - l[(len(l) // 2) - 1])
