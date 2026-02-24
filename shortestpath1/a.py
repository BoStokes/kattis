from collections import *
from heapq import *
from sys import stdin

input = lambda:stdin.readline().rstrip()

INF = float('inf')
while True:
    V, E, Q, s = map(int, input().split())
    if V == 0: exit()

    adj = defaultdict(list)

    for _ in range(E):
        u, v, w = map(int, input().split())
        adj[u].append([v, w])

    dist = [INF] * V
    dist[s] = 0
    pq = [(0, s)]

    while pq:
        d, u = heappop(pq)
        if d > dist[u]: continue
        for v, w in adj[u]:
            if d+w < dist[v]:
                dist[v] = d+w
                heappush(pq, (d+w, v))

    for _ in range(Q):
        node = int(input())
        d = dist[node]
        print(d if d != INF else 'Impossible')