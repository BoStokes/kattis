from math import dist

n = int(input())


for i in range(n):
    m = int(input())
    coords = []
    for _ in range(m):
        x, y = map(float, input().split())
        coords.append((x, y))

    edges = []
    for i in range(len(coords)):
        for j in range(len(coords)):
            edges.append((i, j, dist(coords[i], coords[j])))

    parents = [i for i in range(len(coords)+1)]
    def find(x):
        if parents[x] == x:
            return x
        parents[x] = find(parents[x])
        return parents[x]
    def union(x, y):
        parents[find(x)] = find(y)

    total_weight = 0
    for src, dest, weight in sorted(edges, key=lambda x: x[2]):
        if find(src) != find(dest):
            union(src, dest)
            total_weight += weight
    print(total_weight)