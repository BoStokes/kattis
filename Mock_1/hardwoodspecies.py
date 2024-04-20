from sys import stdin, stdout
from collections import Counter
from heapq import heappush, heappop

heap = []
tree_count = Counter()
total = 0
for species in stdin:
    if species not in tree_count:
        heappush(heap, species)
    tree_count[species] += 1
    total += 1

while heap:
    species = heappop(heap)
    stdout.write(f'{species} {100*tree_count[species]/total}\n')
