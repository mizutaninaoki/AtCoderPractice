# see: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
# -----------------------------------------------------------------------
# 以下の方法はTESTCASE1とTESTCASE2でrowの順番が違うため、間違いになる
# -----------------------------------------------------------------------
# n = int(input())
# titles = input()
# ans = 0
# for i in range(n):
#     row = input()
#     mark = row.split()[1]
#     ans += int(mark)

# print(format(ans / n, '.2f'))


from collections import namedtuple

N = int(input())
Student = namedtuple('Student', input())
print(sum(int(Student(*input().split()).MARKS) for i in range(N)) / N)
