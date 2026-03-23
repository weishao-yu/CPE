T = int(input())
for i in range(1, T + 1):
    costs = []
    for _ in range(4):
        costs.extend(list(map(int, input().split())))
    x = int(input())
    if i > 1:
        print()
    print(f"Case {i}:")
    for _ in range(x):
        min_cost = float('inf')
        number = int(input())
        cheap_base = []
        for base in range(2, 37):
            current_cost = 0
            temp = number
            if temp == 0:
                current_cost = costs[0]
            else:
                while temp > 0:
                    digit = temp % base
                    current_cost += costs[digit]
                    temp = temp // base
            if current_cost < min_cost:
                min_cost = current_cost
                cheap_base = [base]
            elif current_cost == min_cost:
                cheap_base.append(base)
            print(cheap_base)
            print(current_cost)
        print(f"Cheapest base(s) for number {number}:", *cheap_base)
# costs.extend(...)：把 4 行輸入變成 1 行長長的清單，方便查表。