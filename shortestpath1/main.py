# DIJKSTRA'S ALGORITHM

from collections import defaultdict
from heapq import heappush, heappop
from sys import stdin

get_line = lambda: stdin.readline().strip()

while True:
    inp = get_line()
    if inp == '0 0 0 0': exit()
    num_nodes, num_edges, num_queries, source = map(int, inp.split())

    graph = defaultdict(list)

    for _ in range(num_edges):
        src, dest, weight = map(int, get_line().split())
        graph[src].append((dest, weight))

    visited = dict() # Node: Cost

    pq = [(0, source)] # distance, node
    while pq and len(visited) <= num_nodes:
        distance, curr = heappop(pq)
        if curr in visited:
            continue
        visited[curr] = distance
        for next, cost in graph[curr]:
            if next not in visited:
                heappush(pq, (distance + cost, next))

    for _ in range(num_queries):
        query = int(get_line())
        print(visited[query] if query in visited else 'IMPOSSIBLE')
