from collections import *
from functools import cache

n, q = map(int, input().split())

graph = defaultdict(set)
for _ in range(n-3):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)


islands = defaultdict(dict)
get_island = dict()
visited = [False] * (n+1)
island_num = 1
for station in range(1, n+1):
    if not visited[station]:
        island_graph = islands[island_num]
        stack = [station]
        while stack:
            current = stack.pop()
            if visited[current]:
                continue
            get_island[current] = island_num
            island_graph[current] = graph[current]
            visited[current] = True
            for nbr in graph[current]:
                if not visited[nbr]:
                    stack.append(nbr)
        island_num += 1

get_centers = dict()
get_dist_from_center = dict()
get_dist_from_edge = dict()
get_width = dict()
for island_num, island_graph in islands.items():
    # perform kahn's algorithm to find the center of each island tree
    degree = dict()
    leaves = []
    for station in island_graph:
        degree[station] = len(graph[station])
        if degree[station] in (0, 1):
            leaves.append(station)
            degree[station] = 0
    count = len(leaves)
    while count < len(island_graph):
        new_leaves = []
        for node in leaves:
            for nbr in graph[node]:
                degree[nbr] -= 1
                if degree[nbr] == 1:
                    new_leaves.append(nbr)
        count += len(new_leaves)
        leaves = new_leaves
    get_centers[island_num] = leaves

    # now perform bfs from the centers and find the furthest distance to a leaf
    visited = set()
    width = 0
    queue = deque(((node, 0) for node in get_centers[island_num]))
    while queue:
        node, steps = queue.popleft()
        if node in visited: continue
        visited.add(node)
        for nbr in graph[node]:
            if nbr not in visited:
                queue.append((nbr, steps + 1))
        get_dist_from_center[node] = steps
        width = max(width, steps)
    
    get_width[island_num] = 2 * width + len(get_centers[island_num])

@cache
def get_dist_from_edge(station):
    island_num = get_island[station]
    return 1 + get_dist_from_center[station] + get_width[island_num] // 2

for _ in range(q):
    start_station, end_station = map(int, input().split())
    start_island, end_island = get_island[start_station], get_island[end_station]

    middle_island = start_island ^ end_island

    total = get_dist_from_edge(start_station) + get_width[middle_island] + get_dist_from_edge(end_station)
    print(total)