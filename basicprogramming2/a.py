from collections import defaultdict
from math import floor, ceil

N, t = map(int, input().split())
nums = list(map(int, input().split()))

if t == 1:
    seen = set()
    for i, num in enumerate(nums):
        if 7777 - num in seen:
            print('Yes')
            exit()
        seen.add(num)
    print('No')

elif t == 2:
    print('Unique' if len(nums) == len(set(nums)) else "Contains duplicate")

elif t == 3:
    min = N / 2
    count = defaultdict(int)
    for num in nums:
        count[num] += 1
        if count[num] > min:
            print(num)
            exit()
    print(-1)

elif t == 4:
    nums.sort()
    print(*nums[floor((N-1)/2) : ceil((N-1)/2 + 1)])

elif t == 5:
    print(*(num for num in sorted(nums) if 100 <= num <= 999))