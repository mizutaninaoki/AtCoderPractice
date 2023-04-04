# 正直この解答のコード、よくわからない。シフト演算がよくわかっていない。
def countBits(self, num: int) -> List[int]:
    counter = [0]
    for i in range(1, num+1):
        # see:https://leetcode.com/problems/counting-bits/solutions/656849/python-simple-solution-with-clear-explanation/
        # iを２進数にした時の値を右に１だけシフトして、また10進数に戻した時の値(i >> 1)がcounterの配列の添え字になる
        # ビットシフト1は 2 で除算するのと同じ(２進数の桁を左にずらして、１桁削除しているから。
        # 10進数であれば数字に0をつけて、１桁増やすと10倍、1桁減らすと10分の1になるのと同じで、２進数であれは、１桁増やすと２倍になり、１桁減らすと2分の1になる。)
        counter[i] = counter[i >> 1] + i % 2
    return counter


# １つ１つ２進数に変換して、「1」の数をカウントする全探索な方法（あまり良くない）
class Solution:
    def countBits(self, num: int) -> List[int]:
        return [bin(i).count('1') for i in range(num+1)]
