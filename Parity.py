while True:
    try:
        n = int(input())
        if n == 0:
            break
        bin_n = str(bin(n))[2:]
        result = 0
        for i in bin_n:
            if i == '1':
                result += 1
        print(f"The parity of {bin_n} is {result} (mod 2).")
    except EOFError:
        break
# 十進位 -> 二進位	bin(10)	'0b1010'
# 十進位 -> 十六進  hex(10)	'0xa'