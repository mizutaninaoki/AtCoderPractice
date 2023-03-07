# ABCD E F Z
# x
# y
# z

# a : 1
# b : 1
# c : 1
# d : 1
# e : 1
# f : 1
# g : 0
# h : 0
# i : 0
# j : 0
# k : 0
# l : 0
# m : 0
# n : 0
# o : 0
# p : 0
# q : 0
# r : 0
# s : 0
# t : 0
# u : 0
# v : 0
# w : 0
# x : 1
# y : 1
# z : 2

import sys

s = sys.stdin.read().lower()
a = {chr(i): 0 for i in range(ord("a"), ord("z") + 1)}

for i in s:
    if ord(i) in range(ord("a"), ord("z") + 1):
        a[i] += 1

[print(f"{k} : {v}") for k, v in a.items()]
