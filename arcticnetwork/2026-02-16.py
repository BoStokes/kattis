from heapq import *
from math import *

for _ in range(int(input())):
    S, P = map(int, input().split())
    coords = [tuple(map(int, input().split())) for _ in range(P)]

    visited = {0}
    pq = []
    for i in range(1, P):
        heappush(pq, (dist(coords[0], coords[i]), i))

    total_weight = 0
    costs_used = []
    while pq:
        w, u = heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        heappush(costs_used, -w)

        for v in range(P):
            if v in visited: continue
            heappush(pq, (dist(coords[u], coords[v]), v))
    
    for _ in range(S-1):
        heappop(costs_used)
    print(f'{-heappop(costs_used):.2f}')

    
