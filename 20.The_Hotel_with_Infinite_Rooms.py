import math
while True:
    try:
        n, D = map(int,input().split())
        total_D = D + (n * (n - 1) ) // 2
        k = (-1 + math.sqrt(1 + 8 * total_D)) / 2
        answer = math.ceil(k)
        print(answer)  
    except EOFError:
        break 