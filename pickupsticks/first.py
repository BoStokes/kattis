# Kahn's Algorithm

from sys import stdin
from collections import deque

n, m = map(int, next(stdin).strip().split())
edges = [[] for _ in range(n)]
in_degrees = [0] * (n + 1)
for _ in range(m):
    source, dest = map(int, next(stdin).strip().split())
    edges[source].append(dest)
    in_degrees[dest] += 1

available = deque()
for i, v in enumerate(in_degrees):
    if v == 0:
        available.append(i)


topo = []
while available:
    curr = available.popleft()
    topo.append(curr)
    for dest in edges[curr]:
        in_degrees[dest] -= 1
        if in_degrees[dest] == 0:
            available.append(dest)

valid = True
for value in in_degrees:
    if value > 0:
        valid = False
if valid:
    print(*topo, sep='\n')
else:
    print('IMPOSSIBLE')