import sys
# from operator import itemgetter
import heapq

def find(node):
    if parents[node] != node:
        parents[node] = find(parents[node])
    return parents[node]
def union(node1, node2):
    parent1 = find(node1)
    parent2 = find(node2)
    if parent1 != parent2:
        if rank[parent1] > rank[parent2]:
            parents[parent2] = parent1
        elif rank[parent1] < rank[parent2]:
            parents[parent1] = parent2
        else:
            parents[parent2] = parent1
            rank[parent1] += 1


input = sys.stdin.read
data = input().split()
index = 0

n = int(data[index])
index += 1

heap = []
for u in range(1, n + 1):
    for v in range(1, n + 1):
        dist = int(data[index])
        index += 1
        if u < v:
            heapq.heappush(heap, (dist, u, v))

parents = list(range(n+1))
rank = [0] * (n + 1)

while heap:
    dist, u, v = heapq.heappop(heap)
    if find(u) != find(v):
        union(u, v)
        print(u, v)