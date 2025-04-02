from collections import defaultdict

n, m = map(int, input().split())
rungs = [int(input()) for _ in range(m)]

perm = [i for i in range(0, n+1)]
for rung in rungs:
    perm[rung], perm[rung+1] = perm[rung+1], perm[rung]
print(*perm[1:], sep='\n')