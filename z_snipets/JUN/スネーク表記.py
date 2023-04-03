"""
1. 以下のようなスネーク表記を出力してください
 1   5   9   3   7   1   5   9   3   7   1   5   9
0 2 4 6 8 0 2 4 6 8 0 2 4 6 8 0 2 4 6 8 0 2 4 6 8 
   3   7   1   5   9   3   7   1   5   9   3   7  
   
2. 以下のようなスネーク表記を出力してください(縦の行数は変更できるようにしてください)
     f                 x                 p          
    e g               w y               o q         
   d   h             v   z             n   r        
  c     i           u     a           m     s       
 b       j         t       b         l       t      
a         k       s         c       k         u     
           l     r           d     j           v    
            m   q             e   i             w   
             n p               f h               x z
              o                 g                 y 
"""

from typing import List
# 1問目の解答


def snake_string_v1(chars: str) -> List[List[str]]:
    result = [[], [], []]
    result_indexes = {0, 1, 2}
    insert_index = 1
    for i, s in enumerate(chars):
        # １行目の数字(1,5,9...は4で割るとあまりは1になる)
        if i % 4 == 1:
            insert_index = 0  # 1行目に挿入したいから、インデックスを0に設定する
        # 2行目の数字(0,2,4...は2で割るとあまりは0になる)
        elif i % 2 == 0:
            insert_index = 1  # 2行目に挿入したいから、インデックスを1に設定する
        # 3行目の数字(3,7,1...は4で割るとあまりは3になる)
        elif i % 4 == 3:
            insert_index = 2  # 3行目に挿入したいから、インデックスを2に設定する
        result[insert_index].append(s)
        # result_indexes({0,1,2})の集合から挿入するインデックス(insert_index)を排除して、残ったresultの配列には空白を入れる
        for rest_index in result_indexes - {insert_index}:
            result[rest_index].append(' ')
    return result

# 2番目の方の解答


def snake_string_v2(chars: str, depth: int) -> List[List[str]]:
    # 深さ(depth)の分だけの二重配列を用意する(深さの分だけ、１行目、２行目... と表示できるように)
    result = [[] for _ in range(depth)]
    # 値を入れるインデックスの集合を用意{0,1,2,3...のようなやつ}
    result_indexes = {i for i in range(depth)}
    insert_index = int(depth / 2)  # 最初は真ん中の列からスタート

    # 一番上の行まで到達したら、次からは下向きに表示させていきたいため、インデックスを１づつ足していくメソッドを用意
    def pos(i): return i + 1
    # 一番下の行まで到達したら、次からは上向きに表示させていきたいため、イインデックスを１づつ引いていくメソッドを用意インデックスを１づつ足していくメソッドを用意
    def neg(i): return i - 1
    op = neg  # 最初は

    for s in chars:
        result[insert_index].append(s)
        # result_indexes({0,1,2...})の集合から挿入するインデックス(insert_index)を排除して、残ったresultの配列には空白を入れる
        for rest_index in result_indexes - {insert_index}:
            result[rest_index].append(" ")
        # 挿入するインデックスが0になれば(一番上の行に到達)、今度は下向きに表示を変更させたいので、posのメソッドに切り替える
        if insert_index <= 0:
            op = pos
         # 挿入するインデックスがdepth - 1になれば(一番下の行に到達)、今度は上向きに表示を変更させたいので、negのメソッドに切り替える
        if insert_index >= depth - 1:
            op = neg
        # 挿入するインデックス(insert_index)をpos or negのメソッドに従って、増減させて、表示位置を変更していく
        insert_index = op(insert_index)
    return result


if __name__ == "__main__":
    numbers = [str(i) for j in range(5) for i in range(10)]
    strings = "".join(numbers)
    for line in snake_string_v1(strings):
        print("".join(line))

    import string
    alphabet = [s for _ in range(2) for s in string.ascii_lowercase]
    strings = "".join(alphabet)
    for line in snake_string_v2(strings, 10):
        print("".join(line))
