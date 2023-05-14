# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict
d = defaultdict(list)

n, m = map(int, input().split())

for i in range(1, n+1):
    A = input()
    d[A].append(i)

for _ in range(m):
    B = input()
    if d[B]:
        print(*d[B])
    else:
        print(-1)
