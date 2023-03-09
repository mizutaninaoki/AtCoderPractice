# 20 3
# 5 10 15

# 10


# この問題の肝は「一周のうち、移動していない距離が最大の組み合わせ」を選ぶこと。
# つまり、「一周(K) - (出発した家 + 最後の家)」の距離が最大の組み合わせの距離が答えになる
k, n = map(int, input().split())
l = list(map(int, input().split()))

# 配列の中の、２つの家の位置を引く。つまり、家同士を移動した時、歩かなかった距離が出る。
d = [l[i+1] - l[i] for i in range(n-1)]
# 注意点として、家1から家Nへの最短経路は湖のスタートを通らないので最初に別途計算しておく。
d.append(k - l[-1] + l[0])

ans = k
for j in range(n):
    # d[j]には、最初の家から最後の家まで移動した時、湖一周で歩かなかった距離が入ってりう。
    # そのためk-d[j]で移動した距離が算出されるため、この値が一番最小の値を答えとして取得する。
    ans = min(ans, k-d[j])

print(ans)

# ---------------------
# お手本の解答
# ---------------------
# k, n = map(int, input().split())
# root = list(map(int, input().split()))

# d = [root[i+1] - root[i] for i in range(n-1)]
# d.append(k-root[-1]+root[0])
# ans = k

# for j in range(n):
#     ans = min(ans, k-d[j])
# print(ans)
