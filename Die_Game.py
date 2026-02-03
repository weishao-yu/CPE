while True:
    try:
        top = 1
        north = 2
        west = 3
        n = int(input())
        if n == 0:
            break
        for i in range(n):
            command = input()
            if command == 'east':
                top, north, west = west, north, 7 - top
            elif command == 'west':
                top, north, west = 7 - west, north, top
            elif command == 'north':
                top, north, west = 7 - north, top, west
            else:
                top, north, west = north, 7 - top, west
        print(top)
    except EOFError:
        break