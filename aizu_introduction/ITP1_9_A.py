# computer
# Nurtures computer scientists and highly skilled computer engineers
# who will create and exploit knowledge for the new era
# Provides an outstanding computer environment
# END_OF_TEXT

# 3


# from collections import Counter
# import sys

w = input()

cnt = 0
while True:
    s = input()
    if s == "END_OF_TEXT": break

    cnt += s.lower().split(" ").count(w)
print(cnt)
