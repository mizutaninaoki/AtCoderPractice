# -----------------------
# 自分の解答(AC)
# -----------------------
n = int(input())
s = input()

l = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = ""
for i in s:
    for idx, j in enumerate(l):
        if i == j:
            result += l[idx+n]
            break

print(result)


# -----------------------
# 他者の解答
# -----------------------
n = int(input())
s = input()
ans = ''
for i in s:
    a = ord(i)+n
    if a >= 91:
        a -= 26
    ans += chr(a)
print(ans)
