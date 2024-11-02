from heapq import heappush, heappop
from math import dist

n = int(input())
for _ in range(n):
    num_islands = int(input())
    islands = [tuple(map(float, input().split())) for _ in range(num_islands)]
    
    total_dist = 0
    num_edges = 0
    visited = [False] * num_islands

    min_heap = [(0, 0)] # weight, node

    while num_edges < num_islands:
        cost, node = heappop(min_heap)
        if visited[node]:
            continue
        visited[node] = True
        total_dist += cost
        num_edges += 1

        for i in range(num_islands):
            if not visited[i]:
                c = dist(islands[node], islands[i])
                heappush(min_heap, (c, i))
    print(total_dist)