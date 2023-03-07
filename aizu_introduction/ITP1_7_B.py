# 5 9
# 0 0

# 2


while True:
    n, x = map(int, input().split())
    
    if (n, x) == (0,0):
        break
    
    cnt = 0
    for i in range(1, n+1):
        for j in range(1+i, n+1):
            for k in range(1+j, n+1):
                if i+j+k == x:
                    cnt += 1

    print(cnt)