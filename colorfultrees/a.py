from collections import *

n = int(input())
colors = {i:int(input()) for i in range(1, n+1)}

adj = defaultdict(list)
edges = []
for _ in range(n-1):
    a, b = map(int, input().split())
    edges.append((a, b))
    adj[a].append(b)
    adj[b].append(a)

# find a leaf
node = 1
visited = set()
while len(adj[node]) > 1:
    visited.add(node)
    for nbr in adj[node]:
        if nbr not in visited:
            node = nbr
            break
start = node
print(start)
# count colors
u_count = Counter() # starting node will be first u
u_count[colors[start]] += 1

v_count = Counter()
node = 0

