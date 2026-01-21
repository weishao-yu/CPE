def function(A, B):
    A.reverse()
    B.reverse()
    n = max(len(A), len(B))
    while len(A) < n:
        A.append(0)
    while len(B) < n:
        B.append(0)
    CA = 0
    carry = 0
    for i in range(n):
        if A[i] + B[i] + CA > 9:
            carry += 1
            CA = 1
        else:
            CA = 0
    return carry
while True:
    try:
        str_A, str_B = input().split()
        A = list(map(int, str_A))
        B = list(map(int, str_B))
        if A == [0] and B == [0]:
            break
        else:
            result = function(A, B)
        if result == 0:
            print("No carry operation.")
        elif result == 1:
            print(f"1 carry operation.")
        else:
            print(f"{result} carry operations.")
    except EOFError:
        break