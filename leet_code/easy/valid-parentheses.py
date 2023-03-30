class Solution(object):
	def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in s:
            # この場合、keyがループしてiに代入されていく
            if i in d:  # 1
                stack.append(i)
            # stackが0、もしくは左の括弧に対応した右の括弧でない場合、Falseを返す。pop()に引数を指定しない場合は、末尾を削除
            elif len(stack) == 0 or d[stack.pop()] != i:  # 2
                return False
        return len(stack) == 0  # 3

# 1.左の括弧であれば、スタックに追加する。
# 2. else 右括弧でスタックが空（一致する左括弧がないことを意味する）か、左括弧が一致しない場合。
# 3.最後に、スタックにまだマッチしていない左括弧があるかどうかを確認する。
