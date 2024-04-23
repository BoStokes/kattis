# PRIMS ALGORITHM (FASTER)

from heapq import heappush, heappop, heapify
from math import dist

N = int(input())
for _ in range(N):
    num_sat_channels, num_outposts = map(int, input().split())
    nodes = [tuple(map(int, input().split())) for _ in range(num_outposts)]

    # src, dest, cost
    # edges = [(i, j, dist(node1, node2)) for i, node1 in enumerate(nodes) for j, node2 in enumerate(nodes) if i != j]
    # print(*sorted(edges, key=lambda x: x[2]), sep='\n')

    # src: dest, cost
    edges = {
        i: [(j, dist(nodes[i], nodes[j])) for j in range(num_outposts) if i != j] for i in range(num_outposts)
    }

    mst = []
    visited = {0}
    total_weight = 0
    curr_edges = [
        (cost, 0, dest) for dest, cost in edges[0]
    ]
    heapify(curr_edges)

    while curr_edges and len(visited) < num_outposts:
        cost, src, dest = heappop(curr_edges)
        if dest not in visited:
            visited.add(dest)
            mst.append((src, dest, cost))
            total_weight += cost

            for c_dest, c_cost in edges[dest]:
                if c_dest not in visited:
                    heappush(curr_edges, (c_cost, dest, c_dest))
    mst.sort(key=lambda edge: edge[2])

    for _ in range(1, num_sat_channels):
        mst.pop()
    print(f"{mst[-1][2]:.2f}")

