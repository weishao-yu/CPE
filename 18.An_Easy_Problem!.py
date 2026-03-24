while True:
    try:
        line = input()
        sum_digit = 0
        max_digit = 0
        has_valid_num = False
        for char in line:
            val = -1
            if '0' <= char <= '9':
                val = int(char)
            elif 'A' <= char <= 'Z':
                val = ord(char) - ord('A') + 10
            elif 'a' <= char <= 'z':
                val = ord(char) - ord('a') + 36
            
            if val != -1:
                has_valid_num = True
                sum_digit += val
                if val > max_digit:
                    max_digit = val

        if has_valid_num == False:
            continue

        found = False
        base = max(max_digit + 1, 2)
        for n in range(base, 63):
            if sum_digit % (n - 1) == 0:
                print(n)
                found = True
                break

        if not found:
            print(f"such number is impossible!")
    except EOFError:
        break
