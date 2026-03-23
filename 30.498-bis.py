def function(X, num):
    count = 0
    result = 0
    for i in range(len(num) - 2, -1, -1):
        result += num[i] * ((X ** count) * (count + 1)) 
        count += 1
    return result
while True:
    try:
        X = int(input())
        num = list(map(int, input().split()))
        result = function(X, num)
        print(result)
    except EOFError:
        break