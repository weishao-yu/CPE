def judge(N, num):
    result = set()
    if num[0] < 1:
        return False
    for z in range(N - 1):
        if num[z] >= num[z + 1]:
            return False 
    for i in range(N):
        for j in range(i, N):
            a = num[i] + num[j]
            if a not in result:
                result.add(a)
            else:
                return False
    return True
    
count = 1
while True:
    try:
        N = int(input())
        num = list(map(int ,input().split()))
        if judge(N, num):
            print(f"Case #{count}: It is a B2-Sequence.")
        else:
            print(f"Case #{count}: It is not a B2-Sequence.")
        count += 1
    except EOFError:
        break 
