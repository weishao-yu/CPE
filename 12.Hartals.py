def functon(N,hartals_days):
    sleep_day = set()
    for i in range(1, N + 1):
        if i % 7 == 6 or i % 7 == 0:
            continue
        else:
            for j in hartals_days:
                if i % j == 0:
                    sleep_day.add(i)
    return len(sleep_day)
while True:
    try:
        T = int(input())
        for i in range(T):
            N = int(input())
            P = int(input())
            hartals_days = []
            for j in range(P):
                h = int(input())
                hartals_days.append(h)
            result = functon(N, hartals_days)
            print(result)
    except EOFError:
        break
            