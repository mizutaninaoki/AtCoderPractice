from collections import defaultdict
n = int(input())
L = list(map(int, input().split()))
d = defaultdict(int)

for i in L:
    d[i] += 1
    
for v in d.values():
    if v != 1:
        print("NO")
        exit()
print("YES")
