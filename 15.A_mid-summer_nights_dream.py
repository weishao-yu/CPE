while True:
    try:
        n = int(input())
        result = []
        count = 0
        for i in range(n):
            result.append(int(input()))
        result.sort()
        left_mid = (n - 1) // 2
        right_mid = n // 2
        for j in result:
            if result[left_mid] <= j <= result[right_mid]:
                count += 1
        print(f"{result[left_mid]} {count} {result[right_mid] - result[left_mid] + 1}")
    except EOFError:
        break