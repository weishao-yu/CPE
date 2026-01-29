def square(a, b):
    return int(b ** 0.5) - int((a - 1) ** 0.5)
while True:
    try:
        a, b = map(int,input().split())
        if a == 0 and b == 0:
            break
        result = square(a, b)
        print(result)
    except EOFError:
        break