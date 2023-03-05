# 5 4 2 2 1
# Yes

# 5 4 2 4 1
# No

W, H, x, y, r = map(int, input().split())

if x-r < 0 or x+r > W:
    print('No')
elif y-r < 0 or y+r > H:
    print('No')
else:
    print("Yes")