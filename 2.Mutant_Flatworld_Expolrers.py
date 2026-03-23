def Robot(x, y, curr_dir_idx, commands, max_x, max_y, scents):
    orientations = ['N', 'E', 'S', 'W']
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    is_lost = False  # 追蹤是否墜崖

    for cmd in commands:
        if cmd == 'R':
            curr_dir_idx = (curr_dir_idx + 1) % 4
        elif cmd == 'L':
            curr_dir_idx = (curr_dir_idx + 3) % 4
        elif cmd == 'F':
            next_x = x + dx[curr_dir_idx]
            next_y = y + dy[curr_dir_idx]

            if next_x < 0 or next_x > max_x or next_y < 0 or next_y > max_y:
                if scents[x][y] == True:
                    continue  # 氣味保護
                else:
                    scents[x][y] = True  # 原地留下氣味
                    print(f"{x} {y} {orientations[curr_dir_idx]} LOST")
                    is_lost = True
                    break
            else:
                x = next_x
                y = next_y
    if not is_lost:
        print(f"{x} {y} {orientations[curr_dir_idx]}")

max_x, max_y = map(int, input().split())
scents = [[False for _ in range(max_y + 1)] for _ in range(max_x + 1)]
orientations = ['N', 'E', 'S', 'W']

while True:
    try:
        pos_line = input().split()
        if not pos_line:
            continue  
        x, y, dir_char = pos_line        
        x = int(x)
        y = int(y)
        curr_dir_idx = orientations.index(dir_char)
        commands = input().strip()
        Robot(x, y, curr_dir_idx, commands, max_x, max_y, scents)
    except EOFError:
        break 
