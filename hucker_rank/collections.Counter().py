# Enter your code here. Read input from STDIN. Print output to STDOUT
# X = int(input())
# shoes_sizes = set(map(int, input().split()))
# customers = int(input())

# from collections import defaultdict
# d = defaultdict(int)

# for i in range(customers):
#     shoes_size, price = map(int, input().split())

#     if shoes_size not in shoes_sizes or d[shoes_size] + price > 100:
#         continue
#     d[shoes_size] += price

# print(sum(d.values()))


import collections

numShoes = int(input())
shoes = collections.Counter(map(int, input().split()))
numCust = int(input())

income = 0

for i in range(numCust):
    size, price = map(int, input().split())
    if shoes[size]:
        income += price
        shoes[size] -= 1

print(income)
