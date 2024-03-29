# ------------------
# 三角形の成立条件
# ------------------
# 三角形は2つの辺の長さの和は残りの1つの辺の長さより大きいという特徴があります。 つまり、三角形の3辺の長さを a，b，c とするとき、次の三つの不等式が成り立ちます。
# a < b+c
# b < a+c
# c < a+b


# ------------------------------------------------------------------------------------------------------------
# それぞれの値をまとめて乗算してからある数で割った余りと、それぞれの数を乗算して割った余りを繰り返した、最終的なあまりは同じ。
# 大きな桁数の計算は非常に時間がかかるため、計算途中も小さい数に抑えた方が早くなる！
# 他にも、割り算以外は計算途中にあまりをとっても、最終的なあまりと同じ(see: https://qiita.com/drken/items/3b4fdf0a78e7a138cd9a)
# ------------------------------------------------------------------------------------------------------------
print((1 * 2 * 3 * 4 * 5) % 7)
# 1
print(1 * 2 % 7 * 3 % 7 * 4 % 7 * 5 % 7)
# 1
# 他の足し算、引き算も、計算途中の余りをとっても、最終的なあまりは同じ。詳しくは以下参照。
# see: https://math.nakaken88.com/textbook/cp-remainder/


# ------------------------------------------
# ABC299のD問題
# インタラクティブな問題の答え方
# see: https://atcoder.jp/contests/abc299/tasks/abc299_d
# 他者の解答(二分探索法)
# ------------------------------------------
N = int(input())
mi = 1
ma = N
while ma - mi > 1:
    mid = (mi + ma) // 2
    print("?", mid)
    # 必ずwhileの中でprint()の下にインタラクティブな応答を受け付けるinput()を書く！
    ans = int(input())
    if ans == 0:
        mi = mid
    else:
        ma = mid
# 最終的な答えの標準出力はwhileの外に書く！
print("!", mi)
