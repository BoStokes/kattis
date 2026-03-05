from sys import stdin
N = int(input())
nums = [0] + list(map(int, stdin.read().split()))

indices = {nums[i]:i for i in range(N+1)}

tree = [0 for _ in nums]

def ft_sum(k):
    s = 0
    while k >= 1:
        s += tree[k]
        k -= k & -k
    return s

def range_query(start, end):
    return ft_sum(end) - ft_sum(start-1)

def add(k, x):
    if k <= 0:
        return
    while k <= N:
        tree[k] += x
        k += k & -k

for i in range(1, N+1):
    add(i, 1)

def get_tree():
    return [range_query(i,i) for i in range(N+1)]


low_num = 1
high_num = N
i = 1
while low_num <= high_num:
    swaps = 0
    if i % 2 == 1:
        idx = indices[low_num]
        low_num += 1
        swaps = range_query(1, idx-1)
    else:
        idx = indices[high_num]
        high_num -= 1
        swaps = range_query(idx+1, N)
    add(idx, -1)
    print(swaps)
    i += 1