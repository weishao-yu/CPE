def solution(i, j):
    start = min(i, j)
    end = max(i, j)
    max_cycle_length = 0
    for n in range(start, end + 1):
        counter = 1
        current = n
        while current != 1:
            if current % 2 == 1:
                current = current * 3 + 1
            else:
                current = current // 2 
            counter += 1
        max_cycle_length = max(counter, max_cycle_length)
    return max_cycle_length

while True:
    try:
        i, j = map(int, input().split())
        max_cycle_length = solution(i, j)
        print(f"{i} {j} {max_cycle_length}")
    except EOFError:
        break