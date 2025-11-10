from heapq import *
from collections import *
from sys import stdin

n = int(input())

adj = [list(map(int, line.split())) for line in stdin.readlines()]

heap = [(adj[0][i], 0, i) for i in range(1, n)] # src, cost, dest
heapify(heap)

connected = {0}
while heap and len(connected) < n:
    cost, src, dest = heappop(heap)
    if dest in connected:
        continue
    connected.add(dest)
    print(src+1, dest+1)

    for nbr in range(n):
        if nbr in connected:
            continue
        nbr_cost = adj[dest][nbr]
        heappush(heap, (nbr_cost, dest, nbr))
