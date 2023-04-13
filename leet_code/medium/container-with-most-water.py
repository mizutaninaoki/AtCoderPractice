# 自分の解答(全探索。TLE)
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         ans = 0
#         length = len(height)
#         for i in range(length):
#             for j in range(i, length):
#                 # ２本のx軸の距離(j-i) × 2本のy軸の低い方の高さをかけて、面積を算出する
#                 ans = max(ans, (j - i) * min(height[i], height[j]))
#         return ans

# 両端からy軸が低い方の側を中央に向けて、１ずつ狭めていき、その都度最大の面積にならないか計測していく方法
class Solution:
    def maxArea(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1  # 右端のインデックス
        width = len(height) - 1  # 右端のインデックス
        res = 0

        # widthから0にかけて逆順(8,7,6,5,4,3,2,1みたいに進む)にループ(1ループ毎に、ループ内でy軸の位置を1ずつ狭めていくため、それに合わせてwidthの長さも1ずつ小さくなっていく)
        for w in range(width, 0, -1):
            # 左側のy軸の方が低い場合
            if height[L] < height[R]:
                # 左側のy軸を基準に横幅(w)との面積を計算。その後、左側のy軸の位置(L)を右に１ずらす(プラス1する)。
                res = max(res, height[L] * w)
                L = L + 1
            # 右側のy軸の方が低い場合
            else:
                # 右側のy軸を基準に横幅(w)との面積を計算。その後、右側のy軸の位置(L)を左に１ずらす(マイナス1する)。
                res = max(res, height[R] * w)
                R = R - 1
        return res
