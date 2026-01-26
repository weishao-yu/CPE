def GCD(i, j):
    if j == 0:
        return i
    else:
        return GCD(j, i % j)
def function(N):
    G = 0
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            G += GCD(i, j)
    return G
while True:
    try:
        N = int(input())
        if N == 0:
            break
        result = function(N)
        print(result)
    except EOFError:
        break