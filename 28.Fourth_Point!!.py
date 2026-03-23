def function(num):
    p1 = (num[0], num[1])
    p2 = (num[2], num[3])
    p3 = (num[4], num[5])
    p4 = (num[6], num[7])
    if p1 == p3:
        answerX = p2[0] + p4[0] - p1[0]
        answerY = p2[1] + p4[1] - p1[1]
    if p1 == p4:
        answerX = p2[0] + p3[0] - p1[0]
        answerY = p2[1] + p3[1] - p1[1]
    if p2 == p3:
        answerX = p1[0] + p4[0] - p2[0]
        answerY = p1[1] + p4[1] - p2[1]
    if p2 == p4:
        answerX = p1[0] + p3[0] - p2[0]
        answerY = p1[1] + p3[1] - p2[1]
    return answerX, answerY
while True:
    try:
        num = list(map(float, input().split()))
        answerX, answerY = function(num)
        print(f"{answerX:.3f} {answerY:.3f}")
    except EOFError:
        break

# :.3f (你要的)：強制保留 小數點後 3 位。
# 1.2 → 1.200
# 3.14159 → 3.142 (會四捨五入)
# :.3 (不要用)：這代表 3 位有效數字 (Significant Figures)。
# 123.45 → 1.23e+02 (變成科學記號了！❌)
# 0.001234 → 0.00123