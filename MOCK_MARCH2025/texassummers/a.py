from collections import *
from heapq import *

n = int(input())
spots = [tuple(map(int, input().split())) for _ in range(n)]
dorm = tuple(map(int, input().split()))
goal = tuple(map(int, input().split()))


distances = {node: float('inf') for node in spots}
distances[0] = 0
previous = {node: None for node in spots}

pq = []
heappush(pq, )

while pq:
    current_dist, node = heappop(pq)

    for i, nbr in spots:
