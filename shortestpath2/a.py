from collections import *
from heapq import *
from math import ceil
from sys import stdin

input = lambda:stdin.readline().rstrip()
INF = float('inf')

while True:
    V, E, Q, s = map(int, input().split())
    if V == 0: exit()

    adj = defaultdict(list)
    for _ in range(E):
        u, v, t, p, d = map(int, input().split())
        adj[u].append([v, t, p, d])

    arrival = [INF] * V
    pq = [(0, s)]
    arrival[s] = 0
    while pq:
        time, u = heappop(pq)
        if time > arrival[u]: continue

        for v, t, p, d in adj[u]:
            if p == 0 and time > t: continue

            depart = (((time-t + p - 1) // p) * p) + t if p != 0 and time>=t else t
            arrive = depart + d

            if arrive < arrival[v]:
                arrival[v] = arrive
                heappush(pq, (arrive, v))

    for _ in range(Q):
        node = int(input())
        d = arrival[node]
        print(d if d != INF else 'Impossible')