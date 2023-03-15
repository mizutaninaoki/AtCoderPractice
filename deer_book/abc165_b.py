import math
x = int(input())

saving = 100
cnt = 0
while saving < x:
    # saving = math.floor(saving * 1.01)
    saving = saving + saving // 100
    cnt += 1

print(cnt)
