C = int(input())

for _ in range(C):
    m = int(input())
    r = int(input())
    parents = [i for i in range(m+1)]
    def find(x):
        if parents[x] == x:
            return x
        parents[x] = find(parents[x])
        return parents[x]
    def union(x, y):
        parents[find(x)] = find(y)

    for _ in range(r):
        u, v = map(int, input().split())
        union(u, v)
    
    groups = set(find(i) for i in range(m))
    print(len(groups)-1)