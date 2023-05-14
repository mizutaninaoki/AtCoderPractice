from itertools import permutations

s, num = input().split()
num = int(num)

for i in sorted(list(permutations(s, num))):
    print("".join(i))
