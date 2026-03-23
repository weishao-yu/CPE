def function(n, m):
    result = [str(n)]
    if n == 0 or m == 0:
        return False
    while n > 1:
        if n % m == 0:
            result.append(str(n // m))
            n = n // m
        else:
            return False
    return result
while True:
    try:
        n, m= map(int, input().split())
        result = function(n, m)
        if result == False:
            print("Boring!")
        else:
            result = " ".join(result)
            print(result)
    except EOFError:
        break