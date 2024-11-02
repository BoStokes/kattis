from heapq import*
import math
p=input
r=range
for _ in r(int(p())):
 m=int(p());s=[[*map(float,p().split())]for _ in r(m)];d=0;n=0;v=[0]*m;h=[(0,0)]
 while n<m:
  c,i=heappop(h)
  if v[i]:continue
  v[i]=1;d+=c;n+=1
  for j in r(m):
   if~-v[j]:heappush(h,(math.dist(s[i],s[j]),j))
 print(d)