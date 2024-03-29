# see: https://leetcode.com/problems/valid-parentheses/
from collections import Counter


class Solution:
    def isValid(self, s: str) -> bool:
      d = {'(': ')', '{': '}', '[': ']'}
      stack = []
      for i in s:
        if i in d:
          stack.append(i)
        elif len(stack) == 0 or d[stack.pop()] != i:
          return False
      return len(stack) == 0


# see: https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/
# Codilityの問題
def solution(S):
    if len(S) == 0:
        return 0

    d = {"{": "}", "[": "]", "(": ")"}
    stack = []
    for i in S:
        if i in d.keys():
            stack.append(d[i])
        if i in d.values():
            if len(stack) >= 1:
                s = stack.pop()
                if i != s:
                    return 0
            else:
                return 0

    # もしstackに閉じる方のカッコがまだ残っている場合はfalse
    if len(stack) != 0:
        return 0

    return 1
