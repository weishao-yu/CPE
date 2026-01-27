def solve(a, b):
    result = 0
    for i in range(a, b + 1, 2):
        result += i
    return result
while True:
    try:
        T = int(input())
        for i in range(T):
            a = int(input())
            b = int(input())
            if a % 2 == 0:
                a = a + 1
            result = solve(a, b)
            print(f"Case {i+1}: {result}")
    except EOFError:
        break