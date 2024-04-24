import math
m=lambda:map(int,input().split())
for _ in range(*m()):
 h,o=m();r=range(o);n=[list(m())for _ in r];p=[*r];t=0;k=[];e=enumerate
 def f(x):
  if p[x]==x:return x
  p[x]=f(p[x]);return p[x]
 def u(x,y):p[f(x)]=f(y)
 for c,s,d in sorted([(math.dist(n1,n2),i,j)for i,n1 in e(n)for j,n2 in e(n)],key=lambda z:z[0]):
  if f(s)!=f(d):u(s,d);t+=c;k+=[(c,s,d)]
 print(f'{k[-h][0]:.2f}')