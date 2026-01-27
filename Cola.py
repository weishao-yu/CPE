def cola(N):
    if N == 1:
        return 1
    if N == 2:
        return 3
    cola = N
    while cola >= 3:
        new_cola = cola // 3
        empty = cola % 3 + new_cola
        cola = empty
        N += new_cola
    if empty % 3 == 2:
        N += 1
    return N

while True:
    try:
        N = int(input())
        result = cola(N)
        print(result)
    except EOFError:
        break