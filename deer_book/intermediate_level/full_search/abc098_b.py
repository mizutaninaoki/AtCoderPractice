from collections import Counter
n = int(input())
s = input()

ans = 0
for i in range(n):
    # 分割した２つの配列で共通する文字のみ抽出して、数を数える
    cnt = len(Counter(s[:i]) & Counter(s[i:]))
    if cnt > ans:
        ans = cnt
print(ans)
