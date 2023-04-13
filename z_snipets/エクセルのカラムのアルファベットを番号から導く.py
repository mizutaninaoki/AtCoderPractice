# 他者の回答
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while columnNumber > 0:
            # インデックス分を引く必要があるから、columnNumber-1
            result.append(capitals[(columnNumber-1) % 26])
            columnNumber = (columnNumber-1) // 26
        result.reverse()
        return ''.join(result)


# ABCD＝A×26³＋B×26²＋C×26¹＋D＝1×26³＋2×26²＋3×26¹＋4
# ZZZZ＝Z×26³＋Z×26²＋Z×26¹＋Z＝26×26³＋26×26²＋26×26¹＋26
# We can use (n-1)%26 instead, then we get a number range from 0 to 25.
