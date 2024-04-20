line_1 = list(map(int, input().split()))
line_2 = list(map(int, input().split()))
line_3 = list(map(int, input().split()))
line_4 = list(map(int, input().split()))
board = [line_1, line_2, line_3, line_4]

move = int(input())


if move == 1 or move == 3:
    board = [list(line) for line in zip(*board)]
if move == 2 or move == 3:
    board = [line[::-1] for line in board]

board = [[num for num in line if num != 0] for line in board]

for line in board:
    i = 0
    stop = len(line) - 1
    while i < stop:
        if line[i] == line[i + 1]:
            line[i] *= 2
            line.pop(i + 1)
            stop -= 1
        i += 1
    while len(line) < 4:
        line.append(0)

if move == 2 or move == 3:
    board = [line[::-1] for line in board]    
if move == 1 or move == 3:
    board = [list(line) for line in zip(*board)]

for line in board:
    print(" ".join(map(str, line)))