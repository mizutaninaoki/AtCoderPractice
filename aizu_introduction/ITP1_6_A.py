# 5
# 1 2 3 4 5

# 5 4 3 2 1


#
# sortedを使用すると、「*」でなぜか展開できない。。。
#
# n = int(input())
# a = sorted(list(map(int, input().split())), reverse=True)
# print(*a)

#
# OKな回答
#
n = int(input())
a = list(map(int, input().split()))
a.reverse()
print(*a)