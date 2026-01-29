import datetime
while True:
    try:
        T = int(input())
        for i in range(T):
            m , d = map(int, input().split())
            dt = datetime.date(2011, m, d)
            print(dt.strftime("%A"))
    except EOFError:
        break