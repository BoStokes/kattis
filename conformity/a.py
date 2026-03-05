from collections import *
from sys import *

input=lambda:stdin.readline().rstrip()

N = int(input())
common = Counter(tuple(sorted(map(int, input().split()))) for _ in range(N)).most_common()
best = common[0][1]
ans = 0
for _, count in common:
    if count == best:
        ans += best
    else:
        break
print(ans)