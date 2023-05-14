from collections import deque

n = int(input())
que = deque()
for _ in range(n):
    cmd, *num = input().split()
    if num:
        num = int(num[0])

    if cmd == "append":
        que.append(num)
    elif cmd == "appendleft":
        que.appendleft(num)
    elif cmd == "pop":
        if que:
            que.pop()
    elif cmd == "popleft":
        if que:
            que.popleft()
print(*que)
