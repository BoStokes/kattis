from collections import defaultdict
from sys import stdin
input = stdin.readline

n = int(input())
seen = set()
count = 0

dirs = [
    (-2018, 0),
    (0, -2018),
    (0, 2018),
    (2018, 0),
    (-1680, -1118),
    (-1680, 1118),
    (-1118, -1680),
    (-1118, 1680),
    (1118, -1680),
    (1118, 1680),
    (1680, -1118),
    (1680, 1118),
]

seen = {tuple(map(int, input().split())) for _ in range(n)}

for x, y in seen:
    for dx, dy in dirs:
        if (x+dx, y+dy) in seen:
            count += 1

print(count // 2)