from collections import *


n = int(input())


graph = defaultdict(set)
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)