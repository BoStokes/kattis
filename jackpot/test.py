from functools import reduce as r
from math import gcd
i=input
for _ in range(int(i())):i();a=r(lambda a,b:a*b//gcd(a,b),map(int,i().split()));print(a if a<=10**9 else'More than a billion.')