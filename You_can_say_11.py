def function(N):
    odd = 0
    even = 0
    for i in range(len(N) - 1, -1, -2):
        odd += int(N[i])
    for j in range(len(N) - 2, -1, -2):
        even += int(N[j])
    return abs(odd - even) % 11  == 0
while True:
    try:
        N = input()
        if N == "0":
            break
        if function(N):
            print(f"{N} is a multiple of 11.")
        else:
            print(f"{N} is not a multiple of 11.")
    except EOFError:
        break
