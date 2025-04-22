from collections import defaultdict
from heapq import heappush, heappop

while True:
    n, m, q, s = map(int, input().split())
    if n == 0:
        break

    graph = defaultdict(dict)

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u][v] = w

    final = [-1] * n
    pq = [(0, s)]

    while pq:
        dist, node = heappop(pq)
        if final[node] != -1:
            continue
        final[node] = dist
        for nbr in graph[node]:
            if final[nbr] == -1:
                heappush(pq, (dist + graph[node][nbr], nbr))

    for _ in range(q):
        b = int(input())
        print(final[b] if final[b] != -1 else 'Impossible')

    print()
