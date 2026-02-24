from collections import *
from sys import stdin

input = lambda:stdin.readline().strip()

for i in range(int(input())):
    adj = defaultdict(set)
    x, y = 0, 0
    input()
    s = int(input())
    for _ in range(s):
        dir = input()
        u = (x,y)
        if dir == 'N':
            v = (x,y+1)
            y += 1
        elif dir == 'E':
            v = (x+1, y)
            x += 1
        elif dir == 'S':
            v = (x, y-1)
            y -= 1
        elif dir == 'W':
            v = (x-1, y)
            x -= 1
        adj[u].add(v)
        adj[v].add(u)
    food = (x,y)

    dist = {(0,0):0}
    q = deque([(0,0)])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    print(dist[food])