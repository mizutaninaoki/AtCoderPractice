n, t = map(int, input().split())
cl = list(map(int, input().split()))
rl = list(map(int, input().split()))

player1_c = cl[0]
player1_r = rl[0]
cuu_r = -1
ans = -1
ans2 = 1
ans2_idx = player1_r
for idx, (c, r) in enumerate(zip(cl, rl)):
    if c == t and r > cuu_r:
        ans = idx + 1
        cuu_r = r
    elif player1_c == c and r > ans2_idx:
        ans2 = idx + 1
        ans2_idx = r
        

if ans == -1:
    print(ans2)
else:
    print(ans)
    
        
        
    
    