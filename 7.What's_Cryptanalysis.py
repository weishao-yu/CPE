n = int(input())
result = {}
for i in range(n):
    sentence = input().upper()
    for char in sentence:
        if char.isalpha():
            if char in result:
                result[char] += 1
            else:
                result[char] = 1
    new_result = sorted(result.items(), key = lambda x: (-x[1], x[0]))
for j in new_result:
    print(f"{j[0]} {j[1]}")
#先執行變成tuple 然後sorted 用key=指定我要用lambda出來的函式跟原本的資料綁定 sorted就按照新函式去排順序原資料
#為什麼不能直接使用sorted,因為在此題假如直接sorted 他就會按照英文字母 因為是獨一無二的