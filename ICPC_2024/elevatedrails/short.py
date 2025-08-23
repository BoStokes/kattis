from collections import*
j=deque
v=range
w=lambda l,i:l.append(i)
m=lambda:map(int,input().split())
n,q=m()
g=[[]for _ in v(n+1)]
for _ in v(n-3):s,e=m();w(g[s],e);w(g[e],s)
o={}
t=[]
for a in v(1,n+1):
 if len(t)==3:break
 if a in o:continue
 u=len(t)+1;z=j();w(z,a);d=set()
 while z:
  c=z.popleft();o[c]=u;d.add(c)
  for b in g[c]:
   if b not in o:w(z,b)
 w(t,d)
f={}
r={}
l=[0]
for u,h in enumerate(t):
 d={};z=j();p=0
 for x in h:
  d[x]=len(g[x])
  if len(g[x])==1:w(z,x)
 while len(d)>2:
  for _ in v(len(z)):
   x=z.popleft()
   for b in g[x]:
    if b not in d:continue
    d[b]-=1
    if d[b]==1:w(z,b)
   del d[x]
  p+=1
 f[u+1]=p;k=d.keys();w(l,k);z=j(k);p=0
 while z:
  for _ in v(len(z)):
   x=z.popleft()
   if x in r:continue
   r[x]=p
   for b in g[x]:
    if b not in r:w(z,b)
  p+=1
for _ in v(q):s,e=m();w=o[s];y=o[e];x=w^y;print(r[s]+f[w]+len(l[w])+2*f[x]+len(l[x])+r[e]+f[y]+len(l[y]))