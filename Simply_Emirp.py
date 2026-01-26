def Prime(N):
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return False
    return True 
while True:
    try:
        N = int(input())
        if Prime(N) == True:
            reverse_N = str(N)
            reverse_N = int(reverse_N[::-1])
            if Prime(reverse_N) == True and reverse_N != N:
                print(f"{N} is emirp.")
            else:
                print(f"{N} is prime.")
        else:
            print(f"{N} is not prime.")
    except EOFError:
        break