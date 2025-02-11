from collections import defaultdict, deque

n, m = map(int, input().split())

in_degrees = [0] * (n+1)
adj = defaultdict(set)

for i in range(m):
    u, v = map(int, input().split())
    if v in adj[u]:
        continue
    adj[u].add(v)
    in_degrees[v] += 1

q = deque()
for node in range(1, n):
    if in_degrees[node] == 0:
        q.append(node)

topo = []
while q:
    node = q.popleft()
    topo.append(node)

    for nbr in adj[node]:
        in_degrees[nbr] -= 1
        if in_degrees[nbr] == 0:
            q.append(nbr)

if any(in_degrees):
    print('IMPOSSIBLE')
    exit()
print(*topo,sep='\n')

