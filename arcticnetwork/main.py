from math import dist

N = int(input())
for _ in range(N):
    num_sat_channels, outposts = map(int, input().split())
    nodes = [tuple(map(int, input().split())) for _ in range(outposts)]

    # src, dest, cost
    edges = [(i, j, dist(node1, node2)) for i, node1 in enumerate(nodes) for j, node2 in enumerate(nodes) if i != j]
    # print(*edges, sep='\n')

    parents = [i for i in range(outposts + 1)]
    def find(x):
        if parents[x] == x:
            return x
        parents[x] = find(parents[x])
        return parents[x]
    def union(x, y):
        parents[find(x)] = find(y)

    total_weight = 0
    mst = list()

    for src, dest, cost in sorted(edges, key=lambda x: x[2]):
        if find(src) != find(dest):
            union(src, dest)
            total_weight += cost
            mst.append((src, dest, cost))
    mst = list(sorted(mst))
    print(mst)
    for _ in range(num_sat_channels):
        popped = mst.pop()
    print(mst)
    print(f'{sum(edge[2] for edge in mst):.2f}')


