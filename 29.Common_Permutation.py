def function(a, b):
    result_a = {} 
    result_b = {}
    for i in a: 
        if i in result_a:
            result_a[i] += 1
        else:
            result_a[i] = 1
    for j in b: 
        if j in result_b:
            result_b[j] += 1
        else:
            result_b[j] = 1
    return result_a, result_b
def solve(result_a, result_b):
    result = ""
    result_sort_a = sorted(result_a)
    for i in result_sort_a:
        if i in result_b:
            count = min(result_b[i], result_a[i])
            result += i * count
    return result
while True:
    try:
        a = input()
        b = input()
        result_a, result_b = function(a, b)
        result = solve(result_a, result_b)
        print(result)
    except EOFError:
        break