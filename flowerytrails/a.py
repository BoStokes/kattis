from heapq import *
from collections import *

V, E = map(int, input().split())

adj = defaultdict(list)
best_edge = defaultdict(lambda: defaultdict(lambda: 1e9))

for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))
    best_edge[u][v] = min(best_edge[u][v], w)
    best_edge[v][u] = min(best_edge[v][u], w)

pq = [(0, 0)] # (dist, node)
dist = [1e9] * V
dist[0] = 0

predecessors = defaultdict(list)

while pq:
    d, u = heappop(pq)

    if d > dist[u]:
        continue

    for v, weight in adj[u]:
        new_dist = d + weight

        if new_dist < dist[v]:
            dist[v] = new_dist
            predecessors[v] = [(u, new_dist)]
            heappush(pq, (new_dist, v))
        elif new_dist == dist[v]:
            predecessors[v].append((u, new_dist))

total_dist = 0
q = deque((V-1,))
visited = set()

while q:
    u = q.pop()
    
    if u in visited:
        continue
    visited.add(u)

    for v, d in predecessors[u]:
        total_dist += best_edge[u][v]
        q.appendleft(v)

print(total_dist * 2)