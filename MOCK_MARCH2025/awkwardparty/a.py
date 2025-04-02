from collections import *

n = int(input())
level = n

seen = dict()

for i, num in enumerate(map(int, input().split())):
    if num in seen:
        level = min(level, i - seen[num])
    seen[num] = i


print(level)