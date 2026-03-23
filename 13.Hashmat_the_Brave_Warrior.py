while True:
    try:
        for i in range(2):
            me, enemy = map(int, input().split())
            print(abs(me - enemy))
    except EOFError:
        break