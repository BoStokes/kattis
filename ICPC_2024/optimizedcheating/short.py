from collections import*
n,m,k=map(int,input().split())
y=set()
for i in range(n):
 x=int(input())
 if-~i==k:c=x
 else:y.add(x)
r=[]
for i in range(m):o,v=input().split();r.append((o,int(v)))
q=deque([(c,0,())])
while q:
 l,s,p=q.popleft()
 if l not in y:print(s,*p,sep='\n');exit()
 for i in range(m):
  o,v=r[i]
  if'+'==o:w=l+v
  elif'-'==o:w=l-v
  elif'*'==o:w=l*v
  else:w=l//v
  if w<0:continue
  q.append((w,s+1,p+(i+1,)))
print(-1)