from collections import defaultdict
N, Q = map(int, input().split())
wealth = defaultdict(int)

for _ in range(Q):
    instruction, *nums = input().split()
    if instruction == 'SET':
        i, x = map(int, nums)
        wealth[i] = x
    elif instruction == 'RESTART':
        val = int(nums[0])
        wealth = defaultdict(lambda:val)
    elif instruction == 'PRINT':
        i = int(nums[0])
        print(wealth[i])