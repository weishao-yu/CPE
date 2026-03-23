def GCD(result1, result2):
    if result2 == 0:
        return result1
    else:
        return GCD(result2, result1 % result2)
def solve(S1, S2):
    length1 = len(S1)
    length2 = len(S2)
    if S1[0] == "0" or S2[0] == "0":
        return False
    if length1 == 1 or length2 == 1:
        return False
    result1 = 0
    result2 = 0
    S1 = S1[::-1]
    S2 = S2[::-1]
    count1 = 0
    count2 = 0
    for i in S1:
        result1 += int(i) * (2 ** count1)
        count1 += 1 
    for j in S2:
        result2 += int(j) * (2 ** count2)
        count2 += 1
    if GCD(result1, result2) == 1:
        return False
    else:
        return True
while True:
    try:
        N = int(input())
        for i in range(N):
            S1 = input()
            S2 = input()
            if solve(S1, S2):
                print(f"Pair #{i + 1}: All you need is love!")
            else:
                print(f"Pair #{i + 1}: Love is not all you need!")
    except EOFError:
        break
#int(字串, 2) 的意思就是：「請把這個字串當作 2 進位，轉換成整數給我」。