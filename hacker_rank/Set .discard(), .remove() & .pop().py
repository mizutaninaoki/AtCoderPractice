# --------------------------------------------------------------------------------
# 以下自分の解答。なぜか間違うし、Discussionのコードも試したがどれもエラーで通らない。。。
# --------------------------------------------------------------------------------
n = int(input())
s = set(map(int, input().split()))
m = int(input())

for _ in range(m):
    cmd, *num = input().split()

    if cmd == "pop":
        if s:
            s.pop()
    elif cmd == "discard":
        s.discard(int(num[0]))
    elif cmd == "remove":
        if int(num[0]) in s:
            s.remove(int(num[0]))

    print(s)

print(sum(s))
