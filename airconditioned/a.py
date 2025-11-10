F=sorted([*map(int,input().split())]for _ in range(int(input())))
C=A=0
for G,B in F:A=min(A,B);C+=G>A;A=B*(G>A)or A
print(C)