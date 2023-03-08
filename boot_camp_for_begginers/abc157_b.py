# 84 97 66
# 79 89 11
# 61 59 7
# 7
# 89
# 7
# 87
# 79
# 24
# 84
# 30


# Yes


a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
a3 = list(map(int, input().split()))
n = int(input())

for i in range(n):
    b = int(input())

    for i, (a1j, a2j, a3j) in enumerate(zip(a1, a2, a3)):
        if a1j == b:
            a1[i] = True
        elif a2j == b:
            a2[i] = True
        elif a3j == b:
            a3[i] = True

all_list = [a1, a2, a3]

for l in all_list:
    if l[0] == l[1] == l[2] == True:
        print("Yes")
        exit()

for i in range(3):
    if a1[i] == a2[i] == a3[i] == True:
        print("Yes")
        exit()

if a1[0] == a2[1] == a3[2] == True or a1[2] == a2[1] == a3[0] == True:
    print("Yes")
    exit()

print("No")
