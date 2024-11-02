from heapq import heappop, heappush

from math import dist

n = int(input())

for _ in range(n):
    num_islands  = int(input())
    coords = []
    for _ in range(num_islands):
        x, y = map(float, input().split())
        coords.append((x,y))


    visited = [False] * num_islands
    total_dist = 0
    curr_edges = [(0,0)] # Node 0 with a weight of 0
    edge_count = 0

    while curr_edges and edge_count < num_islands:
        weight, node = heappop(curr_edges)
        if visited[node] == True:
            continue
        visited[node] = True
        total_dist += weight
        edge_count += 1

        for v:
            if not visited[_end]:
                heappush(curr_edges, ())
        