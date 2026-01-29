def solve(y ,matrix):
    for i in range(y):
        for j in range(y):
            if matrix[i][j] < 0:
                return False
            if matrix[i][j] != matrix[y -1 - i][y - 1 - j]:
                return False
    return True


T = int(input())
for i in range(T):
    x = input().split()
    y = int(x[-1])
    matrix = []
    for j in range(y):
        list1 = list(map(int, input().split()))
        matrix.append(list1)
    if solve(y, matrix) == True:
        print(f"Test #{i+1}: Symmetric.")
    else:
        print(f"Test #{i+1}: Non-symmetric.")
