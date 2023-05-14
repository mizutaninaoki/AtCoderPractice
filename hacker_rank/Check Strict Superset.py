A = set(map(int, input().split()))
n = int(input())

flag = True
for _ in range(n):
    s = set(map(int, input().split()))
    if not A.issuperset(s):
        flag = False
print(flag)
