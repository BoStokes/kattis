# cats

from collections import defaultdict
from heapq import heappop, heappush
from sys import stdin

lines = iter(stdin.readlines())
input = lambda: next(lines).rstrip()

for _ in range(int(input())):
    milk_amount, num_cats = map(int, input().split())

    distances = defaultdict(dict)
    for _ in range(num_cats * (num_cats-1) // 2):
        cat1, cat2, cost = map(int, input().split())
        distances[cat1][cat2] = cost
        distances[cat2][cat1] = cost
    
    visited = set()
    total_cost = 0
    pq = [(0, 0)]

    while len(visited) < num_cats:
        cost, cat = heappop(pq)
        if cat in visited:
            continue

        visited.add(cat)
        total_cost += 1 + cost

        for nbr in range(num_cats):
            if nbr not in visited:
                heappush(pq, (distances[cat][nbr], nbr))

    print('yes' if total_cost <= milk_amount else 'no')