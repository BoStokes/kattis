num_squares, square, magic_num = map(int, input().split())
board = tuple(map(int, input().split()))
visited = set()
hops = 0
while 1 <= square <= num_squares and board[square-1] != magic_num and square not in visited:
    visited.add(square)
    square+=board[square-1]
    hops+=1
if square < 1:
    print('left')
elif square > num_squares:
    print('right')
elif board[square-1] == magic_num:
    print('magic')
else:
    print('cycle')
print(hops)