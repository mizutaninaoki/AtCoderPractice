import itertools

o = input()
e = input()

st = ""
for i, j in itertools.zip_longest(o, e, fillvalue=""):
    st += i+j
print(st)
