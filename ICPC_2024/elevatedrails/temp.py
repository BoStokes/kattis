from collections import*
j=deque
v=range
m=lambda:map(int,input().split())
n,q=m()
g=[[]for _ in v(n+1)]
for _ in v(n-3):s,e=m();g[s].append(e);g[e].append(s)
o=dict()
t=[]
for a in v(1,n+1):
 if len(t)==3:break
 if a in o:continue
 u=len(t)+1;z=j();z.append(a);d=set()
 while z:
  c=z.popleft();o[c]=u;d.add(c)
  for b in g[c]:
   if b not in o:z.append(b)
 t.append(d)
f=dict()
r=dict()
l=[0]
for u,h in enumerate(t):
 d=dict();z=j();p=0
 for node in h:
  d[node]=len(g[node])
  if len(g[node])==1:z.append(node)
 while len(d)>2:
  nodes=len(z)
  for _ in v(nodes):
   node=z.popleft()
   for b in g[node]:
    if b not in d:continue
    d[b]-=1
    if d[b]==1:z.append(b)
   del d[node]
  p+=1
 f[u+1]=p;k=d.keys();l.append(k);z=j(d.keys());p=0
 while z:
  for _ in v(len(z)):
   node=z.popleft()
   if node in r:continue
   r[node]=p
   for b in g[node]:
    if b not in r:z.append(b)
  p+=1
for _ in v(q):s,e=m();w=o[s];y=o[e];x=w^y;print(r[s]+f[w]+len(l[w])+2*f[x]+len(l[x])+r[e]+f[y]+len(l[y]))
 