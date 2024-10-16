from collections import deque

rows, cols = map(int, input().split())
grid = []
for _ in range(rows):
    row = input()
    grid.append(row)

# print(*grid,sep='\n')

end = (rows-1, cols-1)
queue = deque()
visited = set()

def inbounds(row, col):
    return 0 <= row < rows and 0 <= col < cols

def get_neighbors(row, col, jump):
    return (row-jump, col), (row, col-jump), (row, col+jump), (row+jump, col)


queue.append((0,0,0))  # (row, col, moves so far)


while queue:
    row, col, moves = queue.popleft()
    if not inbounds(row, col) or (row, col) in visited:
        continue
    visited.add((row, col))

    if (row, col) == end:
        print(moves)
        exit()

    jump = int(grid[row][col])
    for next_row, next_col in get_neighbors(row, col, jump):
        queue.append((next_row, next_col, moves+1))

print(-1)