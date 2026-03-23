while True:
    try:
        s = input()
        freq = {}
        for i in s:
            code = ord(i)
            if code not in freq:
                freq[code] = 1
            else:
                freq[code] += 1
        sorted_data = sorted(freq.items(), key=lambda x: (x[1], -x[0]))
        for key, value in sorted_data:
            print(f"{key} {value}")
    except EOFError:
        break