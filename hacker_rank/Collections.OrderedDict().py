from collections import OrderedDict
n = int(input())
d = OrderedDict()

for _ in range(n):
    *name, price = input().split()
    name = " ".join(name)
    price = int(price)

    # OrderedDictはdefaultdictみたいに、キーに存在しないものをいきなり+=で繋げるとエラーになる
    if name in d:
        d[name] += price
    else:
        d[name] = price

for k, v in d.items():
    print(k, v)
