from sys import stdin, setrecursionlimit
setrecursionlimit(5000)

lines = [line.strip() for line in stdin]

index = 0
visited = set()


def get_neighbors(x, y):
    return (x, y-1), (x-1, y), (x+1, y), (x, y+1)
def in_bounds(sky, x, y):
    return 0 <= x < len(sky) and 0 <= y < len(sky[x])
def dfs(sky, x, y):
        if not in_bounds(sky, x, y) or (x, y) in visited or sky[x][y] != '-':
            return
        visited.add((x, y))
        for neighbor in get_neighbors(x, y):
            dfs(sky, neighbor[0], neighbor[1])

case_num = 1
while index < len(lines):
    visited = set()  
    m, n = map(int, lines[index].split())
    sky = [lines[i] for i in range(index+1, index+m+1)]
    
   
    stars = 0
    for x in range(len(sky)):
        for y in range(len(sky[0])):
                if in_bounds(sky, x, y) and (x, y) not in visited:
                    a = sky[x][y]
                    if a == '-':
                        stars += 1
                        dfs(sky, x, y)

    print(f'Case {case_num}: {stars}')

    index += m + 1
    case_num += 1
