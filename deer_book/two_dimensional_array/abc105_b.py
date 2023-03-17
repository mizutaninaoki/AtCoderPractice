n = int(input())

for i in range(0, 101, 4):
    for j in range(0, 101, 7):
        if i + j == n:
            print('Yes')
            exit()
print("No")
