from heapq import *
from collections import *
from math import *
from sys import stdin, stdout

n = int(input())

adj = [list(map(int, line.split())) for line in stdin.readlines()]
# edges = sorted((adj[u][v], u, v) for u in range(n) for v in range(n) if v < u)
edges = []
for u in range(n):
    for v in range(u):
        edges.append((adj[u][v], u, v))
edges.sort()


parents = [i for i in range(n)]
rank = [1 for _ in range(n)]

def find(x):
    while parents[x] != x:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x

def union(u, v):
    u, v = find(u), find(v)
    if rank[u] > rank[v]: u, v = v, u
    parents[u] = v
    if rank[u] == rank[v]: rank[v] += 1

edges_used = 0
for w, u, v in edges:
    if find(u) == find(v): continue
    stdout.write(f'{u+1} {v+1}\n')
    union(u, v)
    edges_used += 1
    if edges_used == n-1:
        break
