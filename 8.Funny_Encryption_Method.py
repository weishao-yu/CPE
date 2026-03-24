case = int(input())
for z in range(case):
    n = int(input())
    n1 = int(str(n), 16) 
    x = bin(n)[2:]
    x1 = bin(n1)[2:]
    count1 = 0
    count2 = 0
    for i in x:
        if i == '1':
            count1 += 1
    for j in x1:
        if j == '1':
            count2 += 1
    print(f"{count1} {count2}")



# def dec_to_bin(N):
#     list2 = []
#     counter = 0
#     while N > 0:
#         A = N % 2 
#         list2.append(A)
#         N = N // 2
#     for i in list2:
#         if i == 1:
#             counter += 1
#     return counter
# def hex_to_bin(N):
#     list1 = []
#     hex = 0
#     times = 0
#     while N > 0:
#         A = N % 10
#         list1.append(A)
#         N = N // 10
#     list1.reverse()
#     for i in list1:
#         hex += i * (16 ** times)
#         times += 1
#     list1.clear()
#     counter = 0
#     while hex > 0:
#         A = hex % 2 
#         list1.append(A)
#         hex = hex // 2
#     for i in list1:
#         if i == 1:
#             counter += 1
#     return counter


# while True:
#     try:
#         T = int(input())
#         for i in range(T):
#             N = int(input())
#             result1 = dec_to_bin(N)
#             result2 = hex_to_bin(N)
#             print(f"{result1} {result2}")
#     except EOFError:
#         break