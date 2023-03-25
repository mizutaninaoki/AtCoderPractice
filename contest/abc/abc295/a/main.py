n = int(input())
L = list(input().split())

for i in L:
    for j in ["and", "not", "that", "the", "you"]:
        if i == j:
            print("Yes")
            exit()
print("No")
