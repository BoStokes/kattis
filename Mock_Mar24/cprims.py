from collections import *
from heapq import *
from sys import *
from io import *
n = 4

input_buffer = BytesIO(stdin.buffer.readline())
edges = defaultdict(list)
for u in range(1, n+1):
    for v in range(1, n+1):
        s = input_buffer.read().decode()
        print(s)
'''
mst = {1}
pq = [(cost, 1, dest) for dest, cost in edges[1]]
heapify(pq)

while len(mst) < n:
    cost, src, dest = heappop(pq)
    if dest in mst:
        continue
    mst.add(dest)
    print(src, dest)
    for nbr_dest, nbr_cost in edges[dest]:
        if nbr_dest not in mst:
            heappush(pq, (nbr_cost, dest, nbr_dest))
'''