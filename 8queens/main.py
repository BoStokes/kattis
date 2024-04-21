board = [list(input()) for _ in range(8)]

def search(r, c):
    temp_r = r + 1
    while temp_r < 8:
        if board[temp_r][c] == '*':
            print('invalid')
            exit()
        temp_r += 1

    temp_c = c + 1
    while temp_c < 8:
        if board[r][temp_c] == '*':
            print('invalid')
            exit()
        temp_c += 1

    temp_r = r + 1
    temp_c = c + 1
    while temp_r < 8 and temp_c < 8:
        if board[temp_r][temp_c] == '*':
            print('invalid')
            exit()
        temp_r += 1
        temp_c += 1
    
    temp_r = r + 1
    temp_c = c - 1
    while temp_r < 8 and temp_c >= 0:
        if board[temp_r][temp_c] == '*':
            print('invalid')
            exit()
        temp_r += 1
        temp_c -= 1

queens = 0
for r in range(8):
    for c in range(8):
        if board[r][c] == '*':
            queens += 1
            board[r][c] = '.'
            search(r, c)
            board[r][c] = '*'
print('valid' if queens == 8 else 'invalid')