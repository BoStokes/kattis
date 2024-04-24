n, t = map(int, input().split())
d = sorted([int(input()) for _ in range(n)])
print('YES' if d.pop() >= t*(n-1) else 'NO')