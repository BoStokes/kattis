for _ in range(int(input())):
    M, C = map(int, input().split())

    parents = [i for i in range(M)]
    def find(node):
        if parents[node] == node:
            return node
        parents[node] = find(parents[node])
        return parents[node]
    def union(node1, node2):
        parent1, parent2 = find(node1), find(node2)
        parents[parent2] = parent1

    distances = []
    for _ in range(C * (C-1) // 2):
        distances.append(tuple(map(int, input().split())))
    
    total_cost = 0
    for i, j, cost in sorted(distances, key=lambda t: t[2]):
        if find(i) == find(j):
            continue
        union(i, j)
        total_cost += cost
    print('yes' if total_cost <= M else 'no')
