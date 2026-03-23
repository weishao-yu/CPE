sentence = []
while True:
    try:
        n = input()
        sentence.append(n)
    except EOFError:
        break

if sentence:
    max_len = 0
    for s in sentence:
        if len(s) > max_len:
            max_len = len(s)
    for i in range(max_len):
        result = ""
        for j in range(len(sentence) - 1, -1, -1):
            if i < len(sentence[j]):
                result += sentence[j][i]
            else:
                result += " "
        print(result)