from bisect import bisect_left
from collections import defaultdict
length, height = map(int, input().split())
num_obstacles = length // 2

nums = [int(input()) for _ in range(length)]
stalagmites = sorted(nums[::2])
stalactites = sorted(nums[1::2])

count = defaultdict(int)
best = length

for h in range(1, height+1):
    g_index = bisect_left(stalagmites, h)
    c_index = bisect_left(stalactites, height+1-h)
    obstacle_count = num_obstacles-g_index + num_obstacles-c_index
    count[obstacle_count] += 1
    best = min(best, obstacle_count)

print(best, count[best])