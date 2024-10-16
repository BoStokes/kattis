n, m = map(int, input().split())

parents = [house for house in range(n+1)]

def union(child1, child2):
    parent1 = find(child1)
    parent2 = find(child2)
    parents[parent1] = parent2

def find(child):
    if parents[child] == child:
        return child
    parents[child] = find(parents[child])
    return parents[child]

for _ in range(m):
    union(*map(int, input().split()))

distinct = []
for house in range(1, n+1):
    parent = find(house)
    if parent != find(1):
        distinct.append(house)

if len(distinct) == 0:
    print('Connected')
else:
    print(*distinct, sep='\n')