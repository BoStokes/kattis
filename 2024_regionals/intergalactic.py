from collections import *

num_competitors, num_entries, team_size = map(int, input().split())

# parents = {i:i for i in range(1, num_competitors+1)}
parents = list(range(num_competitors+1))
def find(node):
    if parents[node] == node:
        return node
    parents[node] = find(parents[node])
    return parents[node]
def union(node1, node2):
    parent1 = find(node1)
    parent2 = find(node2)
    parents[parent2] = parent1

graph = defaultdict(set)

for _ in range(num_entries):
    x, y = map(int, input().split())
    union(x, y)
    graph[x].add(y)


teams = defaultdict(list)

for node in range(1, num_competitors+1):
    teams[find(node)].append(node)

count = 0
for team in teams.values():
    if len(team) == team_size:
        if all(node1 in graph[node2] and node2 in graph[node1] for node1 in team for node2 in team if node1 != node2):
            count += 1
print(count)