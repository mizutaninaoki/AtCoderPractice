n = int(input())
l = sorted(list(map(int, input().split())))

result = "Yes"
for i, a in enumerate(l, 1):
    if i != a:
        result = "No"
print(result)
