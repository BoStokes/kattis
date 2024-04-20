from sys import setrecursionlimit
setrecursionlimit(10**6)

r, c = map(int, input().split())
grid = [[char for char in input()] for _ in range(r)]
visited = set()

def neighbors(x, y):
    return (x, y+1), (x+1, y), (x, y-1), (x-1, y)
def inbounds(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def dfs(x, y, dest):
    for dx, dy in neighbors(x, y):
        if inbounds(dx, dy) and (dx, dy) not in visited and grid[dx][dy] == grid[dest[0]][dest[1]]:
            visited.add((dx, dy))
            if (dx, dy) == dest or dfs(dx, dy, dest):
                return True
    return False

for _ in range(int(input())):
    visited = set()
    nums = input().split()
    x1, y1 = (int(nums[0])-1, int(nums[1])-1)
    x2, y2 = (int(nums[2])-1, int(nums[3])-1)
    char = grid[x1][y1]
    if char != grid[x2][y2]:
        print('neither')
    else:
        visited.add((x1, y1))
        if (x1, y1) == (x2, y2) or dfs(x1, y1, (x2, y2)):
            if char == '0': print('binary')
            else:           print('decimal')
        else:
            print('neither')
