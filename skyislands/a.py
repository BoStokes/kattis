from collections import *

n, m = map(int, input().split())


parents = list(range(n+1))

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return find(parents[x])
def union(node1, node2):
    parents[node1] = find(parents[node2])

for _ in range(m):
    union(*map(int, input().split()))
print(parents)
print('YES' if len(set((find(node) for node in parents))) == 2 else 'NO')