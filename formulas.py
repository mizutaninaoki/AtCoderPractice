# 入力をint型を要素とした配列として受け取る
from collections import defaultdict
import heapq
import itertools
import bisect

# インポートセット
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
from heapq import heappop, heappush
from itertools import groupby
from math import ceil, cos, floor, gcd, radians, sin, tan
from sys import setrecursionlimit
setrecursionlimit(10 ** 8)

# 内包表記での辞書生成
d = {x: i for i, x in enumerate(["a", "c", "b"], 1)}
# {'a': 1, 'c': 2, 'b': 3}

# ------------------------------------------
# 累積和(itertools.accumulate)
# ------------------------------------------
# 累積和を算出
l = [1, 2, 3, 4, 5, 6]
print(list(itertools.accumulate(l)))
# [1, 3, 6, 10, 15, 21]

# ------------------------------------------
# unicodeコードポイントからの変換、還元
# ------------------------------------------
# アルファベットの番号(「ord」でunicodeからアルファベットへ変換。「chr」でunicodeからアルファベットに復元)
# >>> ord("a")
# 97
# >>> ord("z")
# 122
# >>> ord("A")
# 65
# >>> ord("Z")
# 90

# ------------------------------------------
# zfill
# ------------------------------------------
# 引数に文字数を指定すると、元の文字列が右寄せされて残り（左側）がゼロで埋められた文字列を返す。
s = '1234'
print(s.zfill(8))
# 00001234
print(type(s.zfill(8)))
# <class 'str'>
# 元の文字列の文字数よりも少ない値を指定した場合は元の文字列のまま変化なし。
print(s.zfill(3))
# 1234

# ------------------------------------------
# zipとzip_longest
# ------------------------------------------
# zipはイテラブルの中で最短の長さのイテレータを返す点に注意が必要です。 以下の様にabc、12の二つの文字列を与えると、長さが2のイテレータを作成します。(短い方が基準となる)
for (x, y) in zip('abc', '12'):
    print(x, y)
# a 1
# b 2
# zipと似たzip_longestという関数も利用できます。 zip_longestはzipと異なり、最長のイテラブルの長さのイテレータを作成します。
# 最長のイテラブル以外のものについて、長さを超えた場合の要素はデフォルトではNoneが返ってきます。None以外の他の値を返すようにしたい場合はfillvalueという引数を与えます。
for (x, y) in itertools.zip_longest('abc', '12', fillvalue='O'):
    print(x, y)
# a 1
# b 2
# c O


# ------------------------------------------
# heapq
# ------------------------------------------
# リストの最大値・最小値から順にn個の要素を取得したい場合、 heapqモジュールを使う方法もある。
# heapqモジュールの関数nlargest(), nsmallest()を使う。この場合、元のリストは変更されない。
# 第一引数に取得する要素の個数、第二引数に対象とするイテラブル（リストなど）を指定する。
l = [3, 6, 7, -1, 23, -10, 18]
print(heapq.nlargest(3, l))
# [23, 18, 7]
print(heapq.nsmallest(3, l))
# [-10, -1, 3]
print(l)
# [3, 6, 7, -1, 23, -10, 18]


# ------------------------------------------
# [].index (リストの要素が重複していない場合)
# ------------------------------------------
# リストの要素が重複していない場合、index()メソッドを使う。
# index()の引数に調べたい値を指定すると0始まりのインデックスが取得できる。
# リストの要素が重複している場合、index()メソッドは最初のインデックスのみを返す。
l = list('abcde')
print(l)
# ['a', 'b', 'c', 'd', 'e']
print(l.index('a'))
# 0
print(l.index('c'))
# 2


# ------------------------------------------
# type()の比較
# ------------------------------------------
# type()を使った型の判定
# type()の返り値と任意の型を比較することで、そのオブジェクトが任意の型であるかを判定できる。
print(type('string') is str)
# True
print(type('string') is int)
# False


# ------------------------------------------
# 判定
# ------------------------------------------
# 文字列が十進数字か判定
str.isdecimal()
# 文字列が数字か判定
str.isdigit()
# 文字列が数を表す文字か判定
str.isnumeric()
# 文字列が英字か判定
str.isalpha()
# 文字列が英数字か判定
str.isalnum()
# 文字列がASCII文字か判定
str.isascii()


# ------------------------------------------
# defaultdict
# ------------------------------------------
# defaultdict はその名前から連想できるかもしれませんが、dict の初期化を関数にしたがって実施する事ができます。そのため存在チェックが不要です。
# dictの場合、まずkey: valueの形を作ってから、valueを操作しないといけない。(いきなり存在しないキーに対して「d[key] += 1」みたいな「キー生成 & 1プラス」みたいなことはできない。)
# valueにintを指定する場合
l = ["a", "b", "c"]
d = defaultdict(int)  # defaultdict(lambda: int())と同じ意味
for i in l:
    d[i] += 1
print(d)
# defaultdict(<class 'int'>, {'a': 1, 'b': 1, 'c': 1})
# d.get('a') # getでもvalueを取得できる
# 1

# valueにlistを指定する場合
l = ["a", "b", "c"]
d = defaultdict(list)  # defaultdict(lambda: list())と同じ意味
for i in l:
    d[i] += 1
print(d)
# defaultdict(<class 'list'>, {'a': ['a'], 'b': ['b'], 'c': ['c']})
# d.get('a') # getでもvalueを取得できる
# ['a']


# ------------------------------------------
# リストの範囲指定に関するTips(listにて、指定で:を入れる場合、はみ出してもout of indexにはならず空のリストが返ってくる。)
# ------------------------------------------
a = ["a", "b", "c"]

# インデックスで4だけ指定すると、エラーになる。
print(a[4])
# IndexError: list index out of range

# 最後より先のインデックスを範囲指定すると、空の配列が返ってくる
print(a[4:])
# []

# 最後より先のインデックスより前を範囲指定すると、値が存在する、つまり全ての配列が返ってくる。
print(a[:4])
# ['a', 'b', 'c']


# ------------------------------------------
# bisect
# ------------------------------------------
# bisectは、ソートされたリストにソートされた状態を保ちながら挿入、挿入する場所を求めることができるライブラリです。
# 二分探索を利用しているため効率よく挿入する場所を見つけることができます。挿入する場所の探索は𝑂(log𝑛)で行えます。

# bisect_leftは、挿入できるリストの添字を返します。同じ値がある場合は、その値の最も左側の添字になります。
li = [2, 5, 8, 13, 13, 18, 25, 30]
ind = bisect.bisect_left(li, 10)
print(ind)
# 3
ind = bisect.bisect_left(li, 13)
print(ind)
# 3

# bisect_rightとbisectは、挿入できるリストの添字を返します。同じ値がある場合は、その値の最も右側の添字になります。
li = [2, 5, 8, 13, 13, 18, 25, 30]
ind = bisect.bisect_right(li, 10)
print(ind)
# 3
ind = bisect.bisect_right(li, 13)
print(ind)
# 5
ind = bisect.bisect(li, 10)
print(ind)
# 3
ind = bisect.bisect(li, 13)
print(ind)
# 5

# insort_leftはリストに値を挿入します。同じ値がある場合は最も左側に挿入します。
li = [2, 5, 8, 13, 13, 18, 25, 30]
bisect.insort_left(li, 13)
print(li)
[2, 5, 8, 13, 13, 13, 18, 25, 30]

# insort_rightとinsortはリストに値を挿入します。同じ値がある場合は最も右側に挿入します。
li = [2, 5, 8, 13, 13, 18, 25, 30]
bisect.insort_right(li, 13)
print(li)
# [2, 5, 8, 13, 13, 13, 18, 25, 30]


# ------------------------------------------
# itertools.combinations
# ------------------------------------------
# リストから組み合わせを生成、列挙

l = ['a', 'b', 'c', 'd']
# 第一引数にイテラブル（リストや集合setなど）、第二引数に選択する個数を渡すと、その組み合わせのイテレータを返す。
c = itertools.combinations(l, 2)
print(type(c))
# <class 'itertools.combinations'>
for v in itertools.combinations(l, 2):
    print(v)
# ('a', 'b')
# ('a', 'c')
# ('a', 'd')
# ('b', 'c')
# ('b', 'd')
# ('c', 'd')

c_list = list(itertools.combinations(l, 2))
print(c_list)
# [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]
print(len(c_list))
# 6


# ------------------------------------------
# itertools.combinations_with_replacement
# ------------------------------------------
# リストから重複組み合わせを生成、列挙

l = ['a', 'b', 'c', 'd']
h = itertools.combinations_with_replacement(l, 2)
print(type(h))
# <class 'itertools.combinations_with_replacement'>
# 第一引数にイテラブル（リストや集合setなど）、第二引数に選択する個数を渡すと、その重複組み合わせのイテレータを返す。
for v in itertools.combinations_with_replacement(l, 2):
    print(v)
# ('a', 'a')
# ('a', 'b')
# ('a', 'c')
# ('a', 'd')
# ('b', 'b')
# ('b', 'c')
# ('b', 'd')
# ('c', 'c')
# ('c', 'd')
# ('d', 'd')

h_list = list(itertools.combinations_with_replacement(l, 2))
print(h_list)
# [('a', 'a'), ('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'b'), ('b', 'c'), ('b', 'd'), ('c', 'c'), ('c', 'd'), ('d', 'd')]
print(len(h_list))
# 10