r,c=map(int,input().split())
while r:
 print(*(''.join(word)for word in zip(*sorted([''.join(word)for word in zip(*[input()for _ in range(r)])],key=lambda s:s.lower()))),sep='\n')
 r,c=map(int,input().split())
 if r!=0:print()