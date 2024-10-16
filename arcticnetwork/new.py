import math
m=lambda:map(int,input().split())
def f(x):
 if p[x]==x:return x
 p[x]=f(p[x]);return p[x]
def u(x,y):p[f(x)]=y
for _ in range(*m()):
 h,o=m();r=range(o);n=[[*m()]for _ in r];p=[*r];t=0;k=[];e=enumerate
 for c,s,d in sorted([(math.dist(a,b),i,j)for i,a in e(n)for j,b in e(n)],key=lambda z:z[0]):
  if f(s)!=f(d):u(s,d);t+=c;k+=[(c,s,d)]
 print(f'{k[-h][0]:.2f}')