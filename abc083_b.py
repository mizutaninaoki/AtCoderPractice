# 20 2 5
# 84
# 20 以下の整数のうち、各桁の和が 
# 2 以上 
# 5 以下なのは 
# 2,3,4,5,11,12,13,14,20 です。これらの合計である 
# 84 を出力します。

n, a, b = map(int, input().split())
ans = 0
for i in range(1, n+1):
    num = sum(list(map(int, list(str(i)))))
    if a <= num <= b:
        ans += i

print(ans)