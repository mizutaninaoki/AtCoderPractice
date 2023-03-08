# 4 10

# 3

a, b = map(int, input().split())

cnt = 0
outlets = 1 # Bは１以上で、絶対１回は電源タップを使う必要があるため、最初１の状態から始めても問題ない。

while True:
    if outlets >= b: break

    outlets += a - 1
    cnt += 1

print(cnt)