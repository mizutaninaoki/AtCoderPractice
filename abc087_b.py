# # 2
# # 2
# # 2
# # 100


# # 0≤A,B,C≤50
# # A+B+C≥1
# # 50≤X≤20,000
# # A,B,C は整数である
# # X は50 の倍数である

a = int(input())
b = int(input())
c = int(input())
x = int(input())

ans = 0
for i in range(0, a+1):
    for j in range(0, b+1):
        if 0 <= (x - (i*500) - (j*100)) // 50 <= c:
            ans += 1

print(ans)

