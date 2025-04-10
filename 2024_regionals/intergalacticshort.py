from collections import*
n,m,k=map(int,input().split())
p=list(range(n+1))
def f(d):
 if p[d]==d:return d
 p[d]=f(p[d]);return p[d]
def u(q,w):p[f(w)]=f(q)
g=defaultdict(set)
for _ in range(m):x,y=map(int,input().split());u(x,y);g[x].add(y)
s=defaultdict(list)
for d in range(1,n+1):s[f(d)].append(d)
print(sum(1 for t in s.values()if len(t)==k and all(d1 in g[d2]and d2 in g[d1]for d1 in t for d2 in t if d1!=d2)))