from sys import*
setrecursionlimit(9**9)
n,m=map(int,input().split())
g=[list(input())for _ in range(n)]
a = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1, 0),(1,1)]
v=lambda r,c:0<=r<n and 0<=c<m and g[r][c]=='#'
def dfs(r, c):
 if not v(r,c):return
 g[r][c] = '.'
 for dr,dc in a:
  dfs(r+dr,c+dc)
count = 0
for r in range(n):
 for c in range(m):
  if v(r,c):dfs(r,c);count+=1
print(count)