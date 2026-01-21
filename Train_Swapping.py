def Bubble_Sort(L, train):
    counter = 0
    for i in range(L - 1):
        for j in range(L - 1 - i):
            if train[j] > train[j + 1]:
                train[j] , train[j + 1] = train[j + 1], train[j]
                counter += 1
    return counter
while True:
    try:
        N = int(input())
        for i in range(N):
            L = int(input())
            train = list(map(int, input().split()))
            result = Bubble_Sort(L, train)
            print(f"Optimal train swapping takes {result} swaps.")
    except EOFError:
        break