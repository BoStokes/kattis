F=sorted([*map(int,input().split())]for _ in range(int(input())))
C=A=0
for(G,B)in F:
 A=min(A,B)
 if G>A:C+=1;A=B
print(C)