g=range
n=input
w,l=map(int,n().split())
a=[[*map(int,n().split())]for _ in g(w)]
q,_=map(int,n().split())
f=[n()for _ in g(q)]
def e(p,r,c):
 s=0
 for i in g(w):
  for j in g(l):
   if i<r or i>=r+len(p)or j<c or j>=c+len(p[0])or f[i-r][j-c]=='.':s+=a[i][j]
 return s
b=0
for _ in g(4):
 f=[*zip(*f[::-1])]
 for i in g(w-len(f)+1):
  for j in g(l-len(f[0])+1):b=max(b,e(f,i,j))
print(b)