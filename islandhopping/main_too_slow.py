'''

PYTHON WAS TOO SLOW

MADE JAVA SOLUTION INSTEAD

'''



from heapq import heapify, heappop, heappush
from math import dist

n = int(input())
for _ in range(n):
    num_islands = int(input())

    islands = [tuple(map(float, input().split())) for _ in range(num_islands)]
    edges = {
        i: [(j, dist(islands[i], islands[j])) for j in range(num_islands) if i != j] for i in range(num_islands)
    }
    
    visited = {0}
    total_weight = 0
    curr_edges = []
    for edge in edges[0]:
        heappush(curr_edges, (edge[1], 0, edge[0]))

    while curr_edges and len(visited) < num_islands:
        cost, src, dest = heappop(curr_edges)
        if dest not in visited:
            visited.add(dest)
            total_weight += cost

            for c_dest, c_cost in edges[dest]:
                if c_dest not in visited:
                    heappush(curr_edges, (c_cost, dest, c_dest))
    print(total_weight)
