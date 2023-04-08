# 自分の解答(TLE)
# import math
# a, b = map(int, input().split())

# gcd = math.gcd

# cnt = 0
# while a >= 1 and b >= 1:
#     gcd_num = gcd(a, b)

#     a = a - gcd_num
#     b = b - gcd_num
#     cnt += 1

# print(cnt)


# 他者の解答
# see: https://atcoder.jp/contests/arc159/submissions/40428307
A, B = map(int, input().split())


def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)


k = abs(A-B)
m = int(k**0.5)+1
if k == 0:
    print(1)
    exit()
P = [k]
for i in range(2, m):
    if k % i == 0:
        P.append(i)
        P.append(k//i)

ans = 0
i = 0
while A >= 1 and B >= 1:
    g = gcd(A, B)
    A //= g
    B //= g
    if min(A, B) == 1 or abs(A-B) == 1:
        ans += min(A, B)
        break
    n = k
    for p in P:
        if A % p == 0:
            continue
        n = min(n, A % p)
    ans += n
    A -= n
    B -= n

print(ans)
