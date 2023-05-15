# Enter your code here. Read input from STDIN. Print output to STDOUT
# from collections import Counter
# counter = Counter([input() for i in range(int(input()))])
# print(len(counter))
# print(counter.items())
# print(*counter.values())


from collections import OrderedDict
n = int(input())

d = OrderedDict()
for i in range(n):
    s = input()
    if s in d:
        d[s] += 1
    else:
        d[s] = 1

print(len(d))
print(*d.values())
