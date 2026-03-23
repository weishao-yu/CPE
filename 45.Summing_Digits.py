def function(n):
    while int(n) >= 10:
        total = 0
        for i in n:
            total += int(i)
        n = str(total)
    return int(n)

while True:
    try:
        n = input()
        if n == "0":
            break
        total = function(n)
        print(total)
    except EOFError:
        break