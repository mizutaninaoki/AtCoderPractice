class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        start, last = 1, x
        # startがlastを超えるまで続ける
        while start <= last:
            # 中央の値を取得
            # start + (last-start)//2のところで(last + start)//2としていないのは、和がオーバーフローしてしまうのを回避するため。
            mid = start + ((last - start) // 2)
            # 中央値の2乗がx以下、かつ、中央値+1の２乗がxより大きければ、その値(mid)は
            # ２乗すればxと同じかそれ以下だが、midにあとプラス１でもすればxより大きい値になってしまう。
            # つまり、midは２乗すればx以下ギリギリの値だということがわかる。
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            # 中央値(mid)を２乗した値がxより大きいということは、midの値が大きすぎるということなので、lastを今の中央値(mid)に設定して。「左半分」の小さな値たちの中でもう一度バイナリサーチをかける
            elif x < mid * mid:
                # 今調べたのが1~8でmidが4だったとすると、次のバイナリサーチでは1~3を探索するようにする
                last = mid - 1
            # 中央値(mid)を２乗した値がxより小さいということは、midの値が小さすぎるということなので、startを今の中央値(mid)+1に設定して。「右半分」の大きな値たちの中でもう一度バイナリサーチをかける
            else:
                # 今調べたのが1~8でmidが4だったとすると、次のバイナリサーチでは5~8を探索するようにする
                start = mid + 1


# その２
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        first, last = 1, x
        while first <= last:
            mid = first + (last - first) // 2
            if mid == x // mid:
                return mid
            elif mid > x // mid:
                last = mid - 1
            else:
                first = mid + 1
        return last
