while True:
    try:
        V , T = map(int, input().split())
        print(2 * V * T)
    except EOFError:
        break