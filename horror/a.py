from heapq import *
from collections import *


V, H, E = map(int, input().split())

score = defaultdict(lambda: float('inf'))
for i in map(int, input().split()):
    score[i] = 0

adj = defaultdict(list)
for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

pq = [(0, i) for i in score]
while pq:
    s, u = heappop(pq)
    if s == float('inf'):
        1/0
    for v in adj[u]:
        if s+1 < score[v]:
            score[v] = s+1
            heappush(pq, (s+1, v))

best_idx = 0
for i in range(1, V):
    if score[i] > score[best_idx]:
        best_idx = i
print(best_idx)