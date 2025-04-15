from collections import *
from heapq import *
T = int(input())

for _ in range(T):
    graph = defaultdict(list)
    vertices, edges = map(int, input().split())

    parents = [i for i in range(vertices+1)]
    def find(x):
        if parents[x] == x:
            return x
        parents[x] = find(parents[x])
        return parents[x]
    def union(x, y):
        parents[find(x)] = find(y)

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    total_weight = 0
    for

