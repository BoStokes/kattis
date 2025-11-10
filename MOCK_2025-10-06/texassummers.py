from heapq import heappop, heappush
from sys import stdin
from collections import *
input = stdin.readline

n = int(input())
start = n
end = n+1

points = [tuple(map(int, input().split())) for _ in range(n+2)]

distances = [float('inf')] * (n+2)
prev = [-1] * (n+2)
distances[start] = 0

heap = [(0, start)] # cost, src, dest
while heap:
    cost, node = heappop(heap)

    if cost > distances[node]:
        continue

    if node == end:
        break

    for nbr in range(n+2):
        if nbr == node:
            continue
        
        dx = points[node][0] - points[nbr][0]
        dy = points[node][1] - points[nbr][1]
        new_cost = cost + dx*dx + dy*dy
        
        if new_cost < distances[nbr]:
            distances[nbr] = new_cost
            prev[nbr] = node
            heappush(heap, (new_cost, nbr))

path = deque()
curr = prev[end]
while curr != start:
    path.appendleft(curr)
    curr = prev[curr]
print(*path if path else '-', sep='\n')