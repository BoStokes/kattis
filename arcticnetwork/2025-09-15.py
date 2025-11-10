from heapq import heappop, heappush
from math import dist

for _ in range(int(input())):
    S, P = map(int, input().split())

    coords = []
    for _ in range(P):
        coords.append(list(map(int, input().split())))

    visited = {0}
    added = []
    pq = []

    for sat in range(1, P):
        heappush(pq, (dist(coords[0], coords[sat]), 0, sat))
    
    while pq and len(visited) < P:
        cost, src, dest = heappop(pq)
        if dest in visited:
            continue
        added.append(cost)
        visited.add(dest)
        for sat in range(0, P):
            if sat == dest:
                continue
            heappush(pq, (dist(coords[dest], coords[sat]), dest, sat))
    added.sort()
    print(f'{added[P-S-1]:.2f}')
    