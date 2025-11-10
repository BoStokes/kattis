m, n = map(int, input().split())

grid = [list(input()) for _ in range(m)]

def valid(i, j):
    return 0 <= i < m and 0 <= j < n and grid[i][j] == '#'


def dfs(i, j):
    if grid[i][j] == '.':
        return
    grid[i][j] = '.'
    
    for nbr_i in range(i-1, i+2):
        for nbr_j in range(j-1, j+2):
            if valid(nbr_i, nbr_j):
                dfs(nbr_i, nbr_j)

count = 0
for i in range(m):
    for j in range(n):
        if valid(i, j):
            dfs(i, j)
            count += 1
        
print(count)