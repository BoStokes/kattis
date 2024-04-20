import math
from sys import stdin

def lcm(*nums):
    ans = 1
    for val in nums:
        ans = (ans * val) // math.gcd(ans, val)
    return ans


n = int(stdin.readline().strip())
for _ in range(n):
    wheels = stdin.readline()
    periodicities = map(int, stdin.readline().strip().split())
    num = lcm(*periodicities)
    if num <= 1000000000:
        print(num)
    else:
        print('More than a billion.')