from heapq import heappush, heappop
from sys import stdin

input = stdin.readline

n = int(input())
coords = [tuple(map(int, input().split())) for _ in range(n)]

start_idx = n
end_idx = n + 1

coords.append(tuple(map(int, input().split())))  # start
coords.append(tuple(map(int, input().split())))  # end

distances = [float('inf')] * (n + 2)
parent = [-1] * (n + 2)

distances[start_idx] = 0
pq = [(0, start_idx)]

while pq:
    cost, node = heappop(pq)

    if cost > distances[node]:
        continue

    if node == end_idx:
        break

    for nbr in range(n + 2):
        if node == nbr:
            continue
        
        dx = coords[node][0] - coords[nbr][0]
        dy = coords[node][1] - coords[nbr][1]
        weight = dx*dx + dy*dy
        
        new_cost = cost + weight

        if new_cost < distances[nbr]:
            distances[nbr] = new_cost
            parent[nbr] = node
            heappush(pq, (new_cost, nbr))

path = []
curr = end_idx
while curr != start_idx and curr != -1:
    prev = parent[curr]
    if prev < n:
        path.append(prev)
    curr = prev

if path:
    print(*path[::-1])
else:
    print('-')