from collections import *

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


    visited = [False] * (n+1)
    curr_nodes = leaves
    count = len(curr_nodes)
    steps = 0
    while count < len(island_graph):
        new_nodes
    
