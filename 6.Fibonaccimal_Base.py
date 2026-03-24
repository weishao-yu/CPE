Fib = [1, 2]
while True:
    next_fib = Fib[-1] + Fib[-2]
    if next_fib > 10**9:
        break
    Fib.append(next_fib)

n = int(input())
for i in range(n):
    result = ""
    x = int(input())
    flag = False
    temp = x
    for f in reversed(Fib):
        if temp >= f:
            result += "1"
            flag = True
            temp -= f
        elif flag == True:
            result += "0"

    print(f"{x} = {result} (fib)")