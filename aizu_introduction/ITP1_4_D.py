# 5
# 10 1 5 4 17

# 1 17 37

n = int(input())
l = list(map(int, input().split()))

minNum = min(l)
maxNum = max(l)
sumNum = sum(l)

print(minNum, maxNum, sumNum)