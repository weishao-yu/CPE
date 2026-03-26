def get_steps(x, y):
    n = x + y
    return (n * (n + 1)) // 2 + x

n = int(input())

for i in range(1, n + 1):
    x1, y1, x2, y2 = map(int, input().split())
    
    answer = get_steps(x2, y2) - get_steps(x1, y1)
    
    print(f"Case {i}: {answer}")


# def function(x1, y1, x2, y2):
#     result1, result2 = 0, 0
#     step1, step2 = x1 + y1, x2 + y2

#     result1 += ((step1 + 1) * step1) // 2
#     result1 += x1

#     result2 += ((step2 + 1) * step2) // 2
#     result2 += x2
#     answer = result2 - result1
#     return answer


# n = int(input())
# for i in range(n):
#     x1, y1, x2, y2 = map(int, input().split())
#     answer = function(x1, y1, x2, y2)
#     print(f"Case {i + 1}: {answer}")
