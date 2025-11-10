from heapq import heappop, heappush
from math import dist


for _ in range(int(input())):
    num_islands = int(input())

    islands = [tuple(map(float, input().split())) for _ in range(num_islands)]
    visited = [False] * num_islands

    num_connected = 0
    total_dist = 0
    pq = [(0, 0)] # cost, island

    while num_connected < num_islands:
        cost, island = heappop(pq)
        if visited[island]:
            continue
        visited[island] = True
        total_dist += cost
        num_connected += 1
        for i in range(num_islands):
            if not visited[i]:
                heappush(pq, (dist(islands[island], islands[i]), i))
    
    print(total_dist)