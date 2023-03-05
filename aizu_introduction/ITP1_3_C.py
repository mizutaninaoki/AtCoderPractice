# 3 2
# 2 2
# 5 3
# 0 0

# 2 3
# 2 2
# 3 5


while True:
    l = sorted(list(map(int, input().split())))
    if l == [0,0]:
        break
    else:
        print(l[0], l[1])