h, w = map(int, input().split())

for i in range(h):
    l = []
    L = list(map(int, input().split()))
    for j in L:
        l.append("." if j == 0 else chr(64 + j))
    print(*l, sep="")
