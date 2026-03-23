def function(S):
    num = S.pop(0)
    n = sorted(S)
    x = len(n)
    x = x // 2
    mid = n[x]
    dist = 0
    for i in S:
        dist += abs(mid - i)
    return dist
while True:
    try:
        r = int(input())
        for i in range(r):
            S = list(map(int, input().split()))
            dist = function(S)
            print(dist)
    except EOFError:
        break