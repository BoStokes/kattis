N, M = map(int, input().split())


parents = [i for i in range(N+1)]

def find(node):
    if parents[node] == node:
        return node
    parents[node] = find(parents[node])
    return parents[node]
def union(node1, node2):
    p1 = find(node1)
    p2 = find(node2)
    parents[p1] = p2

for _ in range(M):
    node1, node2 = map(int, input().split())
    union(node1, node2)

flag = True
for i in range(2, N+1):
    if find(i) != find(1):
        flag = False
        print(i)
if flag:
    print('Connected')