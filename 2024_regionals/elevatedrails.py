from sys import stdin
from collections import *

num_stations, num_queries = map(int, stdin.readline().split())

parents = list(range(num_stations+1))
graph = defaultdict(set)
def find(u):
    if parents[u] == u:
        return u
    parents[u] = find(parents[u])
    return parents[u]
def union(u, v):
    graph[u].add(v)
    graph[v].add(u)
    parents[find(v)] = find(u)
for _ in range(num_stations-3):
    u, v = map(int, stdin.readline().split())
    union(u, v)
    
# distinguish stations between 3 islands
island_dict = dict()
island = 1
for station in range(1, num_stations+1):
    if find(station) not in island_dict:
        island_dict[find(station)] = island
        island += 1
        continue
    island_dict[station] = island_dict[find(station)]

island_graphs = defaultdict(dict)
for station in range(1, num_stations+1):
    island_num = island_dict[station]
    island_graphs[island_num][station] = graph[station]
    # del graph[station]

# find the middle of each tree, and keep track of each station's distance form the middle
num_centers = dict()
distance_to_middle_dict = dict()
distance_to_edge_dict = dict()
for island_num, island_graph in enumerate(island_graphs.values(), start=1):
    q = deque()
    degrees = dict()
    for station in island_graph:
        degrees[station] = len(island_graph[station])
        if degrees[station] <= 1:
            q.append(station)
    
    while len(degrees) > 2:
        for _ in range(len(q)):
            station = q.popleft()
            for nbr in island_graph[station]:
                if nbr not in degrees:
                    continue
                degrees[nbr] -= 1
                if degrees[nbr] == 1:
                    q.append(nbr)
            del degrees[station]
    num_centers[island_num] = len(q)

    # now, bfs from centers keeping track of distance
    visited = set()
    q = deque([(node, 0) for node in q])
    while q:
        node, dist = q.popleft()
        if node in visited:
            continue
        distance_to_edge_dict[island_num] = dist
        visited.add(node)
        distance_to_middle_dict[node] = dist
        for nbr in island_graph[node]:
            if nbr not in visited:
                q.append((nbr, dist+1))

for _ in range(num_queries):
    start_station, end_station = map(int, stdin.readline().split())

    start_island = island_dict[start_station]
    end_island = island_dict[end_station]
    middle_island = start_island ^ end_island

    print(distance_to_middle_dict[start_station] + num_centers[start_island] + distance_to_edge_dict[start_island]
        + 2 * distance_to_edge_dict[middle_island] + num_centers[middle_island]
        + distance_to_middle_dict[end_station] + num_centers[end_island] + distance_to_edge_dict[end_island])




