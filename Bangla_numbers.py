def function(Num):
    Num = str(Num)
    long = len(Num)
    if long > 7:
        n1 = Num[-7:]
        n2 = Num[:-7]
        result1 = function2(n1)
        result2 = function(n2)
        if result1:
            return f"{result2} kuti {result1}"
        else:
            return f"{result2} kuti"
    else:
        return function2(Num)
def function2(n):
    result = []
    Num = int(n)
    if Num == 0:
        return ""
    if Num >= 100000:
        lakh = Num // 100000
        result.append(f"{lakh} lakh")
        Num = Num % 100000
    if Num >= 1000:
        hajar = Num // 1000
        result.append(f"{hajar} hajar")
        Num = Num % 1000
    if Num >= 100:
        shata = Num // 100
        result.append(f"{shata} shata")
        Num = Num % 100
    if Num > 0:
        result.append(str(Num))
    answer = " ".join(result)
    return answer    
count = 1
while True:
    try:
        Num = int(input())
        result = function(Num)
        if Num == 0:
            print(f"{count}. 0")
        else:
            print(f"{count}. {result}")
        count += 1
    except EOFError:
        break