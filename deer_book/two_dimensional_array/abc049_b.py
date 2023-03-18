h, w = map(int, input().split())

for i in range(h):
    l = list(input().split())
    for _ in range(2):
        print(*l)
