# 他者の解答
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in {"+", "-", "*", "/"}:
                stack.append(int(i))
            else:  # operand
                # tokensの先のインデックスに入っていたのはa、後のインデックスに入っていたのはb
                b = stack.pop()
                a = stack.pop()

                if i == "+":
                    stack.append(a + b)
                elif i == "-":
                    stack.append(a - b)
                elif i == "*":
                    stack.append(a*b)
                else:
                    stack.append(trunc(a/b))  # truncで小数点以下切り捨て
        # 最後stackに残っているのは、tokensの中の値をポーランド算術で計算した結果の値が入っている。
        return stack[0]
