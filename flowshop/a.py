f=lambda:map(int,input().split())
N,M=f()
t=[[0]*(M+1)]+[[0]+[*f()]for _ in range(N)]
for i in range(1,N+1):
 for j in range(1,M+1):t[i][j]+=max(t[i-1][j],t[i][j-1])
print(*[*zip(*t)][-1][1:])