n = int(input())

edges = []
for u in range(1, n+1):
    for v, dist in enumerate(map(int, input().split()), start=1):
        if u == v:
            continue
        edges.append((dist, u, v))

parents = [i for i in range(n+1)]
def find(node):
    if parents[node] == node:
        return node
    parents[node] = find(parents[node])
    return parents[node]
def union(u, v):
    parents[find(u)] = find(v)


for dist, u, v in sorted(edges):
    if find(u) != find(v):
        union(u, v)
        print(u, v)