n, x = map(int, input().split())
subs = [list(map(float, input().split())) for i in range(x)]

# iにはzipで分解された要素が配列で入っている。
for i in zip(*subs):
    mean_val = sum(i) / x
    print(mean_val)
