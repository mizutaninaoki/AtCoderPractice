n, d = map(int, input().split())
T = list(map(int, input().split()))

for idx, i in enumerate(T[:-1]):
    if T[idx+1] - i <= d:
        print(T[idx+1])
        exit()
        
print(-1)