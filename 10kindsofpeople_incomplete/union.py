from sys import setrecursionlimit
setrecursionlimit(10 * 10**6)

rows, cols = map(int, input().split())
parents = [i for i in range(rows * cols)]
grid = [[int(char) for char in input()] for _ in range(rows)]

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]
def union(x, y):
    parents[find(x)] = find(y)

for row in range(rows):
    for col in range(cols):
        index = row * cols + col
        if row > 0 and grid[row][col] == grid[row-1][col]: # above
            union(index, index - cols)
        if col > 0 and grid[row][col] == grid[row][col-1]: # left
            union(index, index - 1)
        if col < cols-1 and grid[row][col] == grid[row][col+1]: # right
            union(index, index + 1)
        if row < rows-1 and grid[row][col] == grid[row+1][col]: # below
            union(index, index + cols)

for _ in range(int(input())):
    r1, c1, r2, c2 = map(int, input().split())
    source_idx = cols * (r1-1) + c1-1
    dest_idx = cols * (r2-1) + c2-1

    if find(source_idx) == find(dest_idx):
        if grid[r1-1][c1-1] == 1:
            print('decimal')
        else:
            print('binary')
    else:
        print('neither')