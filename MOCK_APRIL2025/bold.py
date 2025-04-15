T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    roots = {i:i for i in range(1, n+1)}
    for _ in range(m):
        x, y = map(int, input().split())
        if roots[y] != roots[x]:
            roots[y] = roots[x]
    unique = {roots[i] for i in range(1, n+1)}
    print(len(unique))

