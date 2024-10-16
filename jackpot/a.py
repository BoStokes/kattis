from functools import*
from math import*
i=input
for _ in range(int(i())):i();a=reduce(lambda a,b:a*b//gcd(a,b),map(int,i().split()));print((a,'More than a billion.')[a>10**9])