def function(N, p, i):
    result = p * ((1 - p) ** (i - 1)) / (1 - ((1 - p) ** N))
    return result
while True:
    try:
        S = int(input())
        for _ in range(S):
            N, p, i = input().split()
            N, p, i = int(N), float(p), int(i)
            if p == 0.0:
                print(f"0.0000")
            else:
                result = function(N, p, i)
                print(f"{result:.4f}")
    except EOFError:
        break
