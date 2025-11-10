from sys import stdin
from functools import cache

lines = stdin.readlines()
for line in lines:
    k, n = map(int, line.split())
    @cache
    def dfs(length, i):
        if i < 0 or i > k or length == 0:
            return 0
        if length == 1:
            return 1
        return dfs(length-1, i-1) + dfs(length-1, i) + dfs(length-1, i+1)
    
    tight = sum(dfs(n, i) for i in range(k+1))
    total = (k+1) ** n
    print(tight / total * 100)