T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    [input() for _ in range(m)]
    print(n-1)