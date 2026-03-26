music = {
    'c':[0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    'd':[0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
    'e':[0, 1, 1, 1, 0, 0, 1, 1, 0, 0],
    'f':[0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
    'g':[0, 1, 1, 1, 0, 0, 0, 0, 0, 0], 
    'a':[0, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
    'b':[0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
    'C':[0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
    'D':[1, 1, 1, 1, 0, 0, 1, 1, 1, 0], 
    'E':[1, 1, 1, 1, 0, 0, 1, 1, 0, 0], 
    'F':[1, 1, 1, 1, 0, 0, 1, 0, 0, 0], 
    'G':[1, 1, 1, 1, 0, 0, 0, 0, 0, 0], 
    'A':[1, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
    'B':[1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
}
test_case = int(input())
for i in range(test_case):
    song = input()
    current_state = [0] * 10
    press_state = [0] * 10
    for j in song:
        if j in music:
            next_state = music[j]
            for k in range(10):
                if current_state[k] == 0 and next_state[k] == 1:
                    press_state[k] += 1
        current_state = next_state
    print(*(press_state))
