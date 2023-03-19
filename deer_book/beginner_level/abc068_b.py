n = int(input())

result = 0
max_cnt = 0
for i in range(1, n+1):
    num = i
    remain = 0
    cnt = 0
    while remain == 0:
        remain = num % 2
        num //= 2
        cnt += 1

    if cnt > max_cnt:
        max_cnt = cnt
        result = i
print(result)
