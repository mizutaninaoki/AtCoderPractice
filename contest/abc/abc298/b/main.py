n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]

ans = True
rotated_A = A
for i in range(4):
    for aj, bj in zip(rotated_A, B):
        for ak, bk in zip(aj, bj):
            if ans and ak == 1 and bk != 1:
                ans = False
                break
    rotated_A = list(zip(*rotated_A[::-1]))
    
    if ans:
        print("Yes")
        exit()
    ans = True
print("No")
        

        