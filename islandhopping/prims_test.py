from heapq import heappush, heappop
from math import dist

inp = [
    '2',
    '3',
    '0.0 0.0',
    '0.0 1.0',
    '1.0 0.0',
    '10',
    '30.0 38.0',
    '43.0 72.0',
    '47.0 46.0',
    '49.0 69.0',
    '52.0 42.0',
    '58.0 17.0',
    '73.0 7.0',
    '84.0 81.0',
    '86.0 75.0',
    '93.0 50.0',
    ][::-1]
input = lambda: inp.pop()

n = int(input())
for _ in range(n):
    num_islands = int(input())
    islands = [tuple(map(float, input().split())) for _ in range(num_islands)]
    
    total_dist = 0
    visited = [False] * num_islands
    min_heap = [(0, 0)] # weight, node
    num_edges = 0

    while min_heap and num_edges < num_islands:
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