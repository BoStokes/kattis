from heapq import heappop, heappush


cases = int(input())
for _ in range(cases):
    num_edges = int(input())
    num_vertices = num_edges * (num_edges-1) // 2
    islands = [tuple(map(float, input().split())) for _ in range(num_edges)]

    parents = [i for i in range(num_vertices+1)]
    def find(x):
        if parents[x] == x:
            return x
        parents[x] = find(parents[x])
        return parents[x]
    def union(x, y):
        parents[find(x)] = find(y)

    #src, dest, weight(distance)
    edges = []
    for i, src in enumerate(islands[:-1]):
        for j, dest in enumerate(islands[i+1:], start=i+1):
            distance = ((dest[0] - src[0])**2 + (dest[1] - src[1])**2)**0.5
            edges.append((i, j, distance))
    edges.sort(key=lambda x: x[2])
    total_distance = 0
    for src, dest, distance in edges:
        if find(src) != find(dest):
            union(src, dest)
            total_distance += distance
    print(total_distance)



