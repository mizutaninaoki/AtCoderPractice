# Enter your code here. Read input from STDIN. Print output to STDOUT

n1 = int(input())
a = set(map(int, input().split()))
n2 = int(input())
b = set(map(int, input().split()))

# 排他的論理和(aとbのどちらか片方だけ存在する値)
ans = sorted(a ^ b)
for i in ans:
    print(i)


# m = int(input())
# set1 = set(map(int, input().split()))
# n = int(input())
# set2 = set(map(int, input().split()))

# diff1 = set1.symmetric_difference(set2)
# diff2 = set2.symmetric_difference(set1)

# diff = diff1.union(diff2)

# sort = sorted(diff)

# for i in sort:
#     print(i)
