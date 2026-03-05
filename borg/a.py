from collections import *
from heapq import *

for _ in range(int(input())):
    cols, rows = map(int, input().split())
    start = None
    grid = [[] for _ in range(rows)]
    num_aliens = 0
    aliens = []
    for i in range(rows):
        for j, c in enumerate(input()):
            if c == 'S':
                start = i,j
            elif c == 'A':
                num_aliens += 1
                aliens.append((i,j))
            grid[i].append(c)

    def nbrs(u):
        r, c = u
        return [(i,j) for i,j in [(r-1,c),(r,c-1),(r,c+1),(r+1,c)]
                if 0 <= i < rows and 0 <= j < cols]
    sources = [start]
    # finds next closest alien using multi-source bfs,
    # overwrites it so it can't be found again
    # 
    # returns (dist, node)
    def next_node():
        q = deque(sources)
        steps = 1
        visited = set(sources)
        while q:
            n = len(q)
            for _ in range(n):
                for v in nbrs(q.pop()):
                    i,j = v
                    if v in visited or grid[i][j] == '#': continue
                    visited.add(v)
                    if grid[i][j] == 'A':
                        grid[i][j] = '#'
                        return steps, v
                    q.appendleft(v)
            steps += 1

    total = 0
    while num_aliens > 0:
        d, u = next_node()
        num_aliens -= 1
        total += d
        sources.append(u)
    print(total)



        