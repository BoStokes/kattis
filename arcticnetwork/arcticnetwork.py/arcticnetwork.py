from math import hypot

n = int(input())


for _ in range(n):
    s, p = map(int, input().split())

    nodes = []
    for _ in range(p):
        x, y = map(int, input().split())
        nodes.append((x,y))

    # edges_lengths = [hypot(x2-x1,y2-y1) for x1, y1 in nodes for x2, y2 in nodes if x1!=x2 and y1!=y2]
    # edges_lengths = edges_lengths[:len(edges_lengths) // 2] 
    
    edges_lengths = []
    for i in range(p):
        for j in range(i+1, p):
            edges_lengths.append((i, j, hypot(nodes[i][0] - nodes[j][0])))

    print(edges_lengths)

    num_vertices = p
    parents = [i for i in range(num_vertices + 1)]

    def find(x):
        if parents[x] == x:
            return x
        parents[x] = find(parents[x])
        return parents[x]
    def union(x, y):
        parents[find(x)] = find(y)

    total_weight = 0
    mst = set()

    for src, dest, weight in sorted(edges_lengths, key=lambda x: x[2]):
        if find(src) != find(dest):
            union(src, dest)
            total_weight += weight
            mst.add((src, dest, weight))
    while (s > 0):
        mst.pop()
        s -= 1
    print(mst)

    print(f'{sum(x[2] for x in mst):.2f}')
    print(f'{mst[-1][2]:.2f}')
    