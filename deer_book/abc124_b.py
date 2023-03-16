n = int(input())
l = map(int, input().split())

prev = 0
cnt = 0
for i in l:
    if i >= prev:
        cnt += 1
        prev = i
print(cnt)
