
# 自分の答え(WA)
# class Solution:
#     def isAlienSorted(self, words: List[str], order: str) -> bool:
#         l = [""] * len(words)
#         for idx, word in enumerate(words):
#             for w in word:
#                 for idx2, i in enumerate(order):
#                     if w == i:
#                         l[idx] += str(idx2)
#                         break

#         for idx3, k in enumerate(l):
#             if idx3 == 0:
#                 prev = k
#                 continue
#             if k < prev:
#                 return False
#         return True


# 他者の解答1
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return words == sorted(words, key=lambda word: [order.index(c) for c in word])


# 他者の解答2
def isAlienSorted(self, words: List[str], order: str) -> bool:
      dict = {}
       for i, o in enumerate(order):
            dict[o] = i

        for i in range(1, len(words)):
            # flag = 1 here means inner loop is break out due to pre less than cur
		# flag = 0 here means inner loop done iteration but two strings length are not equal
            pre, cur, flag = words[i-1], words[i], 0
            for j in range(min(len(pre), len(cur))):
                if dict[pre[j]] < dict[cur[j]]:
                    flag = 1
                    break
                elif dict[pre[j]] > dict[cur[j]]:
                    return False
            if not flag and len(pre) > len(cur):
                return False
        return True
