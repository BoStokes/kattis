from collections import deque
from sys import stdin

rows, cols = map(int, input().split())
grid = [line.strip() for line in stdin.readlines()]

queue = deque()
visited = set()

queue.append((0,0,0))

inbounds = lambda r, c: 0 <= r < rows and 0 <= c < cols

while queue:
    row, col, count = queue.popleft()
    if not inbounds(row, col) or (row, col) in visited:
        continue

    visited.add((row, col))

    if (row, col) == (rows-1, cols-1):
        print(count)
        exit()

    jump = int(grid[row][col])
    for d_row, d_col in (-jump,0), (0, -jump), (0, jump), (jump, 0):
        queue.append((row + d_row, col + d_col, count+1))

print(-1)