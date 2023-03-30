# 入力をint型を要素とした配列として受け取る
import functools
import operator
from collections import deque
import math
import collections
from collections import defaultdict
import heapq
import itertools
import bisect

# インポートセット
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
from heapq import heapify, heappop, heappush
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


# ------------------------------------------------------------------
# heapq(# 優先度付きキュー)(heapqはリストから値を取得、削除を高速化する)
# ------------------------------------------------------------------
# 参考：https://kakedashi-engineer.appspot.com/2020/03/18/heapq/
# リストの最大値・最小値から順にn個の要素を取得したい場合、 heapqモジュールを使う方法もある。
# heapqモジュールの関数nlargest(), nsmallest()を使う。この場合、元のリストは変更されない。
# 第一引数に取得する要素の個数、第二引数に対象とするイテラブル（リストなど）を指定する。
l = [3, 6, 7, -1, 23, -10, 18]
# まずはheapの構築を行う必要があります
heapq.heapify(l)  # リストを優先度付きキューへ
# ヒープ化したlを出力
print(l)
# [-10, -1, 3, 6, 23, 7, 18]

# 順番が入れ替わっていますね。
# リストAはヒープと呼ばれるデータ構造（正確には、Pythonではある規則に従って並び替えられたリスト）となっています。
# ただし、ソートされているわけではありません。
# この時heap[0]で最小値を取得することができます。

print(heapq.heappop(l))  # 最小値の取り出し
# 出力: -10 (l の最小値)
print(l)
# 出力: [-1, 3, 6, 23, 7, 18] (最小値を取り出した後の l)

heapq.heappush(l, -2)  # 要素の挿入
print(l)
# 出力: [-2, -1, 3, 6, 23, 7, 18]   (-2 を挿入後の l)


# 最大値の取り出し
# heapqでは最小値しか取り出すことが出来ません。では最大値の時はどうするかというと、各要素に-1をかけた上で最小値を取り出していきます。
# 以下のコードではmap関数で各要素を-1倍していますが、実際に問題を解く際には入力時に-1した方が高速です。
a = [1, 6, 8, 0, -1]
a = list(map(lambda x: x*(-1), a))  # 各要素を-1倍
print(a)

heapq.heapify(a)
print(heapq.heappop(a)*(-1))  # 最大値の取り出し
print(a)
# 出力
# [-8, -6, -1, 0, 1]
# 8
# [-6, 0, -1, 1]


# 大きい順に３つ取得
print(heapq.nlargest(3, l))
# [23, 18, 7]
print(heapq.nsmallest(3, l))
# [-10, -1, 3]
print(l)
# [3, 6, 7, -1, 23, -10, 18]


# heapqを使うべき場面 まとめ
# ソートされていないリストから小さい順にK個の値を取り出したい場合の計算量は
# sort: O(NlogN)
# heapq: O(N+KlogN)
# となるので、Kの数（取り出したい数）に応じて使い分けるべきです。

# K=1の場合: min
# KがNより十分小さいの場合: heapq
# KとNがほぼ等しい場合: sort
# ただし、後述するように、数を取り出す途中で挿入も発生する場合はheapqを使うべきです。


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


# --------------------------------------------------------------------------
# deque(リストの両端の追加・取り出しを頻繁に行う場合はdequeの方が圧倒的に早い)
# --------------------------------------------------------------------------
# 以下、リストとdequeの使い分け
# 要素の追加・取り出し（削除）・アクセス（取得）が両端のみ → deque
# 両端以外の要素に頻繁にアクセス → リスト

d = deque()
print(d)
# deque([])
print(type(d))
# <class 'collections.deque'>
d = deque(['m', 'n'])
print(d)
# deque(['m', 'n'])

# 要素の追加: append(), appendleft(), extend(), extendleft(), insert()
# append()は末尾（右側）、appendleft()は先頭（左側）に要素を追加する。

# append -> １つ追加
d.append('o')
print(d)
# deque(['m', 'n', 'o'])
d.appendleft('l')
print(d)
# deque(['l', 'm', 'n', 'o'])

# extend()は末尾、extendleft()は先頭にリストなどのイテラブルオブジェクトの要素をすべて追加する。
# extendleft()では引数に指定したイテラブルの要素の順番が逆転して連結されるので注意。dequeの先頭にイテラブルの要素を順番に追加していくイメージ。
# extend -> 複数追加
d.extend(['p', 'q'])
print(d)
# deque(['l', 'm', 'n', 'o', 'p', 'q'])
d.extendleft(['k', 'j'])
print(d)

# insert()で途中に要素を追加することもできる。第一引数に位置、第二引数に追加する値を指定する。
# 第一引数に負の値を指定すると末尾からの位置になる。また、存在しない位置（範囲外の位置）を指定した場合は先頭か末尾に追加される。
d.insert(3, 'XXX')
print(d)
# deque(['j', 'k', 'l', 'XXX', 'm', 'n', 'o', 'p', 'q'])


# 要素の削除: pop(), popleft(), remove(), clear()
# pop()は末尾（右側）、popleft()は先頭（左側）から要素をひとつ削除し、その値を返す。リストのpop()と異なり、引数に位置を指定することはできない。
d = deque(['a', 'b', 'c', 'b', 'd'])
print(d.pop())
# d
print(d)
# deque(['a', 'b', 'c', 'b'])
print(d.popleft())
# a
print(d)
# deque(['b', 'c', 'b'])
# remove()は引数に指定した値と等しい最初の要素を削除する。該当する要素が複数あっても削除されるのは最初の要素のみ。該当する要素がない場合はエラーとなる。
d.remove('b')
print(d)
# deque(['c', 'b'])

# 要素全体をローテート: rotate()
# リストにはないメソッドとしてrotate()がある。デフォルトでは右に1個ずつ要素がローテート（スクロール）する。
d = deque(['a', 'b', 'c', 'd', 'e'])
d.rotate()
print(d)
# deque(['e', 'a', 'b', 'c', 'd'])


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
# (例）
"1".isdigit()
True
"a".isdigit()
False
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
# OrderedDict
# ------------------------------------------
# Pythonの辞書（dict型オブジェクト）は要素の順番を保持しない。OrderedDictは追加した順番通り、要素を保持してくれる
od = collections.OrderedDict()

od['k1'] = 1
od['k3'] = 3
od['k2'] = 2
print(od)
# OrderedDict([('k1', 1), ('k3', 3), ('k2', 2)])



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


# ------------------------------------------
# all（少なくとも１つの条件を求めるときはany()を使う）
# ------------------------------------------
# リストの中が全てTrueの場合、Trueを返す。１つでもFalseがあればFalseを返す。
all([True, True, True])
# True
all([True, True, False])
# False
all([True, True, "a", 2])  # 文字列や数字が混ざっている場合もTrueの対象になる、0や空文字（""）はFalseの対象になる。
# True
# この結果をall(), any()の引数に指定すると、各要素がすべて条件を満たすか、ひとつでも条件を満たすかといった判定ができる。
print(all([i > 2 for i in l]))
# False


# ------------------------------------------
# pop
# ------------------------------------------
# 指定した位置(index)の要素を削除し、値を取得: pop()
# リストのメソッドpop()で、指定した位置の要素を削除し、その要素の値を取得できる。
# 先頭（最初）は0。
l = [0, 10, 20, 30, 40, 50]
print(l.pop(0))
# 0
print(l)
# [10, 20, 30, 40, 50]
print(l.pop(3))
# 40
print(l)
# [10, 20, 30, 50]


# ------------------------------------------
# remove
# ------------------------------------------
# 指定した値(value)と同じ要素を検索し、最初の要素を削除: remove()
# リストのメソッドremove()で、指定した値と同じ要素を検索し、最初の要素を削除できる。
l = ['Alice', 'Bob', 'Charlie', 'Bob', 'Dave']
l.remove('Alice')
print(l)
# ['Bob', 'Charlie', 'Bob', 'Dave']


# ------------------------------------------
# zipで転置
# ------------------------------------------
l = zip([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(l)
# <zip object at 0x102d16f00>
list(l)
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

# 二重配列を天地する場合、変数lに*をつけてやらないといけない！！！
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list(zip(*l)))
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]


# ------------------------------------------
# filter(イテラブル（リストやタプルなど）から条件を満たす要素を抽出したり削除したりできる。)
# ------------------------------------------
# filter()の第一引数に関数（呼び出し可能オブジェクト）、第二引数にリストなどのイテラブルオブジェクトを指定する。
# イテラブルの要素に関数を適用し、結果がTrueと判定されたものを抽出する。
# 値が偶数（2で割ったときのあまりが0）のときTrueを返すlambda（ラムダ式、無名関数）を例とする。

l = [-2, -1, 0, 1, 2]
print(filter(lambda x: x % 2 == 0, l))
# <filter object at 0x10bb38580>
print(type(filter(lambda x: x % 2 == 0, l)))
# <class 'filter'>
# 結果をリストに変換したい場合はlist()を使う。
print(list(filter(lambda x: x % 2 == 0, l)))
# [-2, 0, 2]


# --------------------------------------------------------------
# ループさせる配列自身をループ内で配列自身の要素を削除(popやremove)するとおかしくなる
# --------------------------------------------------------------
# 参考：haya-programming.com/entry/2018/06/02/163415
# 以下のようなコードを書くと、ループが正しく動作しない。
# ループ内で配列自身の要素を削除(popやremove)しないようにするか、内包表記で書くと大丈夫っぽい。
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in lst:
    if x % 2 != 0:
        lst.remove(x)


# ---------------------------------------------------------------------------
# 配列の中に複数の指定する値が存在するかどうか(setを使う もしくは in演算子をand, orで繋げて書く)
# ---------------------------------------------------------------------------
a = ['a', 'b', 'c']
set(a)
# {'c', 'b', 'a'}
set(["a", "b"]) <= set(a)
# True
set(["a", "d"]) <= set(a)
# False


# ---------------------------------------------------------------------------
# math.sqrt(X) は X ** 0.5と一緒
# ---------------------------------------------------------------------------
X = 2
math.sqrt(X)
# 1.4142135623730951
X**0.5
# 1.4142135623730951


# ---------------------------------------------------------------------------------------------
# 集合はset。削除はdiscard。追加はadd(複数はupdate)。重複した値を追加しても、重複した値は追加されない。
# ---------------------------------------------------------------------------------------------
# 配列や辞書よりsetが早い。(集合の場合の削除は常にdiscard使っとけばいいと思う)
a = {'apple', 'lemon', 'peach'}
a.remove('apple')
print(a)
# {'lemon', 'peach'}

# discardもremoveと同じく指定した値を削除できるが、集合に値が存在しなくてもエラーにならない。(removeはエラーになる。)
# 集合の場合は常にdiscard使っとけばいいと思う。
a.discard('apple')
print(a)
# {'lemon', 'peach'}

# next(iter(setのオブジェクト))で集合の最初の値が取得できる
next(iter(a))
# 'lemon'


# update()メソッドの引数にリストやタプルなどを指定することで複数の要素を一度にまとめて追加することができます。
# set.update(追加するコレクション)
vals = {1, 2, 3}
vals.update([1, 4])
print(vals)
# {1, 2, 3, 4}


# ---------------------------------------------------------------------------------------------
# リストの中身を全て掛け算する
# ---------------------------------------------------------------------------------------------
list1 = [1, 3, 4, 10, 4, 45, 90, 100]
print(list1)
#  [1, 3, 4, 10, 4, 45, 90, 100]
# reduce()で要素の掛け算を行う
print(functools.reduce(operator.mul, list1))
# 194400000


# --------------------------------------------------
# evalとexec
# --------------------------------------------------
# 参照：https://qiita.com/kyoshidajp/items/57ae371b3f5d8a84fb13
# eval は第1引数を式として評価します。次は簡単な例です。
eval('1 + 2')
# 3
# exec は第1引数を文として実行します。次は簡単な例です。
exec('a = 1 + 2')
# None (execは代入も可能。そのときはNoneを返す（値を返さない）)


# --------------------------------------------------
# iter, next
# --------------------------------------------------
season = ['Spring', 'Summer', 'Fall', 'Winter']
iter_season = iter(season)
print(type(iter_season))  # 型を表示して確認
#  <class 'list_iterator'>
print(next(iter_season))  # 1番目のイテレータを表示後、次のイテレータに進む
# Spring
# Fall
# Winter
next(iter_season)  # 次のイテレータに進む

# イテレータを１つずつ取り出して表示
for i in iter_season:
    print(i)
# Spring
# Fall
# Winter


# --------------------------------------------------
# startswith
# --------------------------------------------------
str1 = 'あいうえお'
print(str1.startswith('あいう'))  # True
print(str1.startswith('あいえ'))  # False
