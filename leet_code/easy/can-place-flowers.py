# 自分の解答(any()とか使う方法)
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ans = 0
        for i in range(len(flowerbed)):
            # flowerbedの最初、かつ、最初と２番目の花壇が両方0であれば、ansにプラス1する
            if i == 0:
                if any(flowerbed[i:i+2]) == False:
                    flowerbed[i] = 1
                    ans += 1
                continue
             # flowerbedの最後、かつ、最後と最後から２番目の花壇が両方0であれば、ansにプラス1する
            if i == len(flowerbed) - 1:
                if any(flowerbed[i-1:i+1]) == False:
                    flowerbed[i] = 1
                    ans += 1
                continue

            # 上記以外で、「現在の１つ前、現在、現在の１つ後」、３つの花壇が全て0であれば、ansにプラス1する
            if any(flowerbed[i-1:i+2]) == False:
                flowerbed[i] = 1
                ans += 1

        return ans >= n

# 他者の解答


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count, prev = 0, 0

        for cur in flowerbed:
            if cur == 1:
                # 現在が1で、前が1だということは、前のループで花壇に花を植えられないのに、プラス１してしまっているため、マイナス１する。
                if prev == 1:  # violation!
                    count -= 1
                prev = 1
            else:
                if prev == 1:  # can't plant
                    prev = 0
                else:
                    # 次を見ていないが、count1プラスする。次が1だったら、マイナス１する。
                    count += 1
                    prev = 1  # the cur plot gets taken

        return count >= n
