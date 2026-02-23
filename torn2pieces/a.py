from collections import *

n = int(input())

adj = defaultdict(set)
for i in range(n):
    u, *nbrs = input().split()
    for v in nbrs:
        adj[u].add(v)
        adj[v].add(u)

start, end = input().split()

parent = {start:'0'}
used = set()
q = deque()
q.appendleft(start)
used.add(start)
while q:
    u = q.pop()
    for v in adj[u]:
        if v in used: continue
        used.add(v)
        parent[v] = u
        q.appendleft(v)

if end in parent:
    u = end
    path = []
    while u != '0':
        path.append(u)
        u = parent[u]
    print(' '.join(reversed(path)))
else:
    print('no route found')