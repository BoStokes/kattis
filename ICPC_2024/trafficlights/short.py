n=int(input())
l=[[*map(int,input().split())]for _ in range(n)]
s=[0]*n
t=0
while t:=t+1:
 for i,d in enumerate(l):
  r,g=d
  if t%(r+g)>=r:s[i]=1
  else:s[i]=0
 if all(s):
  break
print(t)