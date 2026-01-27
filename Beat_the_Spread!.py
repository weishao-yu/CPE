def function(s, d):
    a = (s + d) // 2
    b = s - a
    return a, b
while True:
    try:
        T = int(input())
        for i in range(T):
            s, d = map(int, input().split())
            if d > s or (s + d) % 2 != 0:
                print("impossible")
            else:    
                a, b = function(s, d)
                print(a, b)
    except EOFError:
        break