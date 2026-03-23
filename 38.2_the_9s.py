while True:
    try:
        n = input()
        if n == '0':
            break
        current_sum = sum(map(int, n))
        if current_sum % 9 != 0:
            print(f"{n} is not a multiple of 9.")
        else:
            degree = 1
            while current_sum > 9:
                current_sum = sum(map(int, str(current_sum)))
                degree += 1
                print(f"{n} is a multiple of 9 and has 9-degree {degree}.")
    except EOFError:
        break
# 一個正整數的各位數字之和（位數和）與原數字在模 3 或模 9 的條件下同餘，這意味著該數與其位數和除以 3 或 9 的餘數相同。