# 5
# 3 1 4 5 4

# 2
# 2 4


n = int(input())
l = list(map(int, input().split()))

l2 = [0]*n

for idx, v in enumerate(l):
    if l2[idx] == 0:
        l2[v-1] = 1

print(l2.count(0))

result = []
for index, j in enumerate(l2):
    if j == 0:
        result.append(index+1)
print(*result)
