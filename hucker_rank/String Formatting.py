def print_formatted(number):
    # ２進数のに変換する一番大きい10進数が最大の空白の幅になる
    bin_len = len(bin(number)[2:])
    for i in range(1, number+1):
        # rjust()で右寄せにする
        dec_num = str(i).rjust(bin_len, " ")
        oct_num = oct(i)[2:].rjust(bin_len, " ")
        hex_num = hex(i)[2:].upper().rjust(bin_len, " ")
        bin_num = bin(i)[2:].rjust(bin_len, " ")

        print(dec_num, oct_num, hex_num, bin_num)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
