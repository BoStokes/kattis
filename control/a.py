from collections import *

class UFdict(dict):
    def __missing__(self, key):
        self[key] = key
        return key

N = int(input())
p = UFdict()
rank = defaultdict(lambda: 1)
setSize = defaultdict(lambda: 1)
numSets = N

def find(x):
    if p[x] == x: return x
    p[x] = find(p[x])
    return p[x]
def union(x, y):
    x, y = find(x), find(y)
    if x == y: return
    if rank[x] > rank[y]: x, y = y, x
    p[x] = y
    if rank[x] == rank[y]: rank[y] += 1
    setSize[y] += setSize[x]
    global numSets
    numSets -= 1

def unionList(r):
    for x in r[1:]:
        union(x, r[0])
    
def valid(recipe):
    parentSizes = 0
    used = set()
    for x in recipe:
        x = find(x)
        if x not in used:
            parentSizes += setSize[x]
            used.add(x)
    return parentSizes == len(recipe)

recipes = [list(map(int, input().split()))[1:] for _ in range(N)]

num_conconted = 0
for r in recipes:
    if valid(r):
        unionList(r)
        num_conconted += 1
print(num_conconted)
