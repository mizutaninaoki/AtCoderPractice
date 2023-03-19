n, m = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(m)]

# 注意： 0の時は「-1」を表示させるようにする
for i in range(1000):
    i_str = str(i)
    if len(i_str) == n:
        flag = True
        for l in L:
            j, k = l
            if i_str[j-1] != str(k):
                flag = False

        if flag:
            print(i)
            exit()
print(-1)
