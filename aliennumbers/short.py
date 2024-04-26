for i in range(int(input())):
 e=enumerate;n,s,t=input().split();b=0;a='';x={c:d for d,c in e(s)};y=len(t)
 for p,d in e(n[::-1]):b+=x[d]*len(x)**p
 while b>0:v=b%y;a=str(t[v])+a;b//=y
 print(f'Case #{i+1}: {"".join(a)}')