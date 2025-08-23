from collections import defaultdict
from sys import stdin

n, m, k = map(int, stdin.readline().split())
# print(n,m,team_size)

parents = [i for i in range(n+1)]
def findParent(competitor):
    if parents[competitor] == competitor:
        return competitor
    parents[competitor] = findParent(parents[competitor])
    return parents[competitor]
def union(competitor1, competitor2):
    parent1 = findParent(competitor1)
    parent2 = findParent(competitor2)
    parents[parent1] = parent2

graph = [[] for _ in range(n+1)]
for _ in range(m):
    competitor1, competitor2 = map(int, stdin.readline().split())
    graph[competitor1].append(competitor2)
    union(competitor1, competitor2)
# print(parents)

teams = defaultdict(list) # teams[parent] = list of competitors with that parent
for competitor in range(1, n+1):
    teams[findParent(competitor)].append(competitor)


# Now check every team to fink teams of size k
count = 0
for parent in teams:
    team = teams[parent]
    if len(team) == k:
        # Make sure that every member of the team points to every other member
        valid = True
        for competitor in team:
            if len(graph[competitor]) != k-1:
                valid = False
                break
        if valid:
            count += 1
        
print(count)